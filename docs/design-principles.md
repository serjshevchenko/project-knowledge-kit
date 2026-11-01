# Framework principles

- **Source of truth:** One canonical file per concern.
- **Bootstrap:** ChatGPT Project Instructions point to the current index; they do not duplicate all rules.
- **Context routing:** Index → applicable rules → minimum relevant source.
- **Lazy retrieval:** No indiscriminate project-wide reads.
- **Current by default:** Latest dated file, old files preserved for history.
- **Fail closed:** Stop if required rules/sources are inaccessible; no cached reconstruction.
- **Transactional maintenance:** Update changelog/README/references with material source changes.
- **Verification:** A generated scaffold is not an applied ChatGPT configuration.
- **Portability:** Templates live in GitHub; installed project sources may live elsewhere.
