import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT.parent / 'docs_restatify-tensegrity-ai'
TRACE = DOCS / 'traceability' / 'README.md'
REQS = DOCS / 'requirements'
PROTO_DIR = ROOT / 'proto' / 'tensegrity' / 'v1'


class TraceabilityRequirementTests(unittest.TestCase):
    def test_traceability_matrix_exists(self):
        self.assertTrue(TRACE.exists(), 'Traceability matrix is missing')
        text = TRACE.read_text(encoding='utf-8')
        self.assertIn('REQ-SYS-001', text)
        self.assertIn('REQ-SYS-012', text)

    def test_key_system_requirements_are_documented(self):
        for req_id in ('REQ-SYS-001', 'REQ-SYS-004', 'REQ-SYS-005', 'REQ-SYS-009', 'REQ-SYS-012'):
            found = False
            for path in REQS.glob('*.md'):
                if req_id in path.read_text(encoding='utf-8'):
                    found = True
                    break
            self.assertTrue(found, f'{req_id} is not described in requirements docs')

    def test_architecture_design_doc_exists(self):
        path = DOCS / 'architecture' / 'komponentendesign.md'
        self.assertTrue(path.exists(), 'Architecture design doc is missing')
        text = path.read_text(encoding='utf-8')
        for marker in ('Core (Rust)', 'Hive (Python)', 'Cloud-Backend (C# / ASP.NET)', 'Uno-App'):
            self.assertIn(marker, text)

    def test_contracts_cover_core_flow(self):
        required = {
            'common.proto',
            'inference.proto',
            'feedback.proto',
            'federation.proto',
            'release.proto',
            'admin.proto',
            'exchange.proto',
        }
        actual = {p.name for p in PROTO_DIR.glob('*.proto')}
        self.assertTrue(required.issubset(actual), f'Missing required proto files: {sorted(required - actual)}')

    def test_traceability_names_follow_requirement_pattern(self):
        text = TRACE.read_text(encoding='utf-8')
        for name in (
            'req_sys_001_confidentiality_level_enum',
            'req_sys_004_fold_clips_and_dp_noise',
            'req_sys_005_nur_lokal_sends_zero_bytes',
            'req_sys_009_release_signature_and_hash_validation',
            'req_sys_012_audit_log_for_blocked_submission',
        ):
            self.assertIn(name, text)


if __name__ == '__main__':
    unittest.main()
