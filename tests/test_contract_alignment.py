import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTO_DIR = ROOT / 'proto' / 'tensegrity' / 'v1'
WORKSPACE = ROOT.parent


def proto_fields(message_name: str, proto_file: str) -> set[str]:
    text = (PROTO_DIR / proto_file).read_text(encoding='utf-8')
    match = re.search(rf'message {message_name} \{{(.*?)\}}', text, re.DOTALL)
    assert match is not None, f'Message {message_name} not found in {proto_file}'
    body = match.group(1)
    fields = set()
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        m = re.search(r'([a-z][a-z0-9_]*)\s*=\s*\d+', line)
        if m:
            fields.add(m.group(1))
    return fields


class ContractAlignmentTests(unittest.TestCase):
    def test_generate_request_fields_match_proto(self):
        expected = proto_fields('GenerateRequest', 'inference.proto')
        self.assertEqual(
            expected,
            {'request_id', 'session_id', 'prompt', 'stream', 'expert_slot_ids', 'max_level'},
        )

    def test_generate_response_fields_match_proto(self):
        expected = proto_fields('GenerateResponse', 'inference.proto')
        self.assertEqual(
            expected,
            {'request_id', 'model_id', 'text', 'selected_expert', 'generated_at'},
        )

    def test_delta_submission_fields_match_proto(self):
        expected = proto_fields('DeltaSubmission', 'federation.proto')
        self.assertEqual(
            expected,
            {
                'submission_id', 'device_id', 'app_instance_id', 'slot_id', 'category',
                'compressed_delta', 'structure_message', 'privacy_round', 'level', 'signature',
            },
        )

    def test_feedback_event_fields_match_proto(self):
        expected = proto_fields('FeedbackEvent', 'feedback.proto')
        self.assertEqual(
            expected,
            {'event_id', 'session_id', 'app_instance_id', 'model_id', 'rating', 'comment', 'level', 'evidence'},
        )

    def test_cloud_core_uses_proto_field_names(self):
        hive_client = WORKSPACE / 'api_restatify-tensegrity-ai-cloud' / 'src' / 'Restatify.Tensegrity.Cloud.Core' / 'HiveClient.cs'
        text = hive_client.read_text(encoding='utf-8')
        for field in ('device_id', 'app_instance_id', 'trust_score', 'source'):
            self.assertIn(field, text, f'Cloud HiveClient must submit proto-aligned field {field}')

    def test_hive_submit_endpoint_uses_proto_field_names(self):
        main = WORKSPACE / 'api_restatify-tensegrity-ai-hive' / 'hive' / '__main__.py'
        text = main.read_text(encoding='utf-8')
        for field in ('device_id', 'app_instance_id', 'trust_score', 'source'):
            self.assertIn(field, text, f'Hive submit endpoint must read proto-aligned field {field}')


if __name__ == '__main__':
    unittest.main()
