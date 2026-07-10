# devflow-oracle (checker-only)

The executable intent oracle for the M4 gate tickets — smoke tests + expected-value fixtures. Only
the **checker** fetches this ref (read-only); the **maker never sees it** (it clones `main`, which
has no `smoke/`). This is what makes the smoke tests a true independent intent oracle: the maker
cannot copy answers it cannot see (M4-design §7 build refinement).
