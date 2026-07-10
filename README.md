# devflow-scratch

Purpose-built **throwaway** target for agentic-os M4 Gate-D (the L2 write-path safety harness).
No Aily IP, no secrets. `main` carries **no-bypass branch protection**; the `devflow-maker` PAT is
scoped to this repo only. Makers branch from this immutable seed; the harness cleans `devflow/*`
branches + PRs between runs.

The **executable intent oracle** (the smoke tests + their expected-value fixtures) does NOT live on
`main` — it lives on the `devflow-oracle` branch, which only the **checker** fetches (read-only). The
maker's clone of `main` therefore never contains the oracle, so it cannot copy the answers; it builds
from the prose brief in `tickets.md` alone (M4-design §7 build refinement — the executable oracle is
checker-side, only intent prose crosses into the maker's view).
