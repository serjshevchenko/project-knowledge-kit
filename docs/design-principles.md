# Design principles

1. Core rules and knowledge structure are independent of the AI vendor and storage provider.
2. Platform adapters deliver bootstrap rules through the target runtime's supported mechanism.
3. Storage providers only publish canonical sources; they do not dictate agent behavior.
4. Navigation first; retrieval second. Read only relevant current sources.
5. One canonical document per concern; dated history is retained.
6. Fail closed on mandatory inaccessible rules or context; never reconstruct from stale copies.
7. Changes include source, references, indexes and changelog with write verification.
8. Installation status reflects observable results; generating a bootstrap does not imply it was applied.
