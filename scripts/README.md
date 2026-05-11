# scripts/

Tooling for the DoView Book. See [ADR-013](../docs/adrs/ADR-013-Iris-Deployment-Script.html).

## `deploy_to_iris_uat.py` — publish to Iris UAT

Walks `docs/md/`, creates a "DoView Book" set (with packages mirroring
the disk layout) inside the "DoView Strategy Models" collection on
https://iris-uat.chrisbarlow.nz, and uploads every `.md` file as an
Iris Text diagram. Intra-corpus markdown links are rewritten to
`iris://diagram/<uuid>` so they navigate inside Iris.

### Setup

```bash
cd scripts
python3 -m venv ../.venv-iris-deploy
source ../.venv-iris-deploy/bin/activate
pip install -r requirements.txt
```

### Run

```bash
# Plan only — prints the package + diagram counts; no writes.
python deploy_to_iris_uat.py --dry-run

# Live deploy.
python deploy_to_iris_uat.py
```

### Env vars

| Var | Default |
|---|---|
| `IRIS_UAT_URL` | `https://iris-uat.chrisbarlow.nz` |
| `IRIS_UAT_USER` | `tester@test.local` |
| `IRIS_UAT_PASSWORD` | `riddlemetest863!` |

### Idempotency

If the "DoView Book" set already exists, the script exits with code 2
and prints the existing-set URL. Delete it via the Iris UI before
re-running, or pass `--set 'DoView Book (rev 2)'` to publish
side-by-side.

## Tests

```bash
cd scripts
python -m pytest tests/ -v
```

Unit tests live in `tests/test_link_rewriter.py` and cover the pure
`link_rewriter.py` module (frontmatter stripping, link rewriting,
code-fence awareness, unknown-link reporting).
