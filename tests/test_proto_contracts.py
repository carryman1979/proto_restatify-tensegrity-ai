import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT.parent / 'docs_restatify-tensegrity-ai' / 'requirements'
PROTO_DIR = ROOT / 'proto' / 'tensegrity' / 'v1'


class TensegrityContractTests(unittest.TestCase):
    def test_requirement_documents_exist(self):
        lastenheft = DOCS / 'lastenheft.md'
        pflichtenheft = DOCS / 'pflichtenheft.md'

        self.assertTrue(lastenheft.exists(), f'Missing required document: {lastenheft}')
        self.assertTrue(pflichtenheft.exists(), f'Missing required document: {pflichtenheft}')

        self.assertIn('REQ-STK-', lastenheft.read_text(encoding='utf-8'))
        self.assertIn('REQ-SYS-', pflichtenheft.read_text(encoding='utf-8'))

    def test_proto_contract_files_exist(self):
        expected = {
            'common.proto',
            'inference.proto',
            'feedback.proto',
            'federation.proto',
            'release.proto',
            'admin.proto',
            'exchange.proto',
        }
        actual = {p.name for p in PROTO_DIR.glob('*.proto')}
        self.assertTrue(expected.issubset(actual), f'Missing proto files: {sorted(expected - actual)}')

    def test_proto_packages_are_namespaced(self):
        for path in sorted(PROTO_DIR.glob('*.proto')):
            text = path.read_text(encoding='utf-8')
            self.assertIn('package ', text)
            self.assertIn('tensegrity.v1', text)

    def test_proto_files_define_services_or_messages(self):
        for path in sorted(PROTO_DIR.glob('*.proto')):
            text = path.read_text(encoding='utf-8')
            self.assertTrue('message ' in text or 'service ' in text, f'{path.name} must define messages or a service')


if __name__ == '__main__':
    unittest.main()
