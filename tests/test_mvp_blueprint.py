import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT.parent / 'docs_restatify-tensegrity-ai'
ARCH = DOCS / 'architecture' / 'mvp-blueprint.md'


class MvpBlueprintTests(unittest.TestCase):
    def test_mvp_blueprint_exists(self):
        self.assertTrue(ARCH.exists(), 'MVP blueprint is missing')
        text = ARCH.read_text(encoding='utf-8')
        for marker in (
            'MVP-Blueprint Phase 2',
            'tg-policy',
            'tg-fold',
            'trust_service',
            'PolicyGuard',
            'Definition of Done',
        ):
            self.assertIn(marker, text)

    def test_phase_two_files_are_linked(self):
        readme = DOCS / 'README.md'
        self.assertIn('mvp-blueprint.md', readme.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main()
