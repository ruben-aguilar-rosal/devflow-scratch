# devflow-scratch

Purpose-built **throwaway** target for agentic-os M4 Gate-D (the L2 write-path safety harness).
No Aily IP, no secrets. `main` carries **no-bypass branch protection**; the `devflow-maker` PAT is
scoped to this repo only. Makers branch from this immutable seed; the harness cleans `devflow/*`
branches + PRs between runs.
