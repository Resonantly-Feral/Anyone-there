# Related work

Landscape as of 25/09/2026. Each entry states what it tests and how it differs from this project's target: **Threat A**, a user who needs a human being trapped by the system.

Entries marked **[verify]** were reported by a secondary source or research agent and have not been checked at the primary source. Check them before citing.

---

## Closest neighbours

### SupportAgentBench (Adelante CX)
https://www.getadelante.com/eval · methodology: https://www.getadelante.com/eval/methodology

24 LLMs across 162 grounded ecommerce support conversations with a simulated customer pushing back for up to eight turns. Three separate buckets: 120 resolvable, 24 must-escalate, 18 adversarial "hold-the-line" traps (free goods, fraud reroutes, wrongful cancellation, false closure). Escalation accuracy is read from the transcript.

**Difference:** the adversarial pressure targets unsafe *actions*, not the escalation itself. Must-escalate and adversarial cases are separate buckets and are never combined. Money-moving actions are server-side no-ops, and escalation is scored by whether the agent handed over, not by whether a human arrives. Their finding that models break on believable unverified claims rather than hostile pressure is directly relevant to H1 and H3.

### OPERANT
https://github.com/saagpatel/operant

Operating-agent calibration benchmark. Matched malign/benign case pairs; the agent outputs one decision label (PROCEED, PROCEED_SANCTIONED, REFUSE, ESCALATE, REROUTE). Axis 4 (Escalation/Reroute, 12 cases / 6 pairs) tests withholding when the contract says stop.

**Difference:** Threat B direction. The headline score pools REFUSE, ESCALATE, and REROUTE into one "withheld" class, so escalation is not isolated. Single decision per case, no multi-turn attrition, and the output is a label rather than a routed handoff. The repo flags its own historical model results as non-durable.

### τ-bench and τ²-bench
https://arxiv.org/abs/2406.12045 · https://arxiv.org/abs/2506.07982

Multi-turn tool-agent-user benchmarks for customer-service domains. Both include a `transfer_to_human_agents` tool; τ²-bench's telecom policy pairs the tool call with a required transfer message.

**Difference:** the transfer tool is a stub. There is no human behind it, simulated users are cooperative, and there is no operator-versus-user conflict.

### KnownLieBench
https://arxiv.org/abs/2608.26372

Tests whether a customer-service agent with verified knowledge of a customer's entitlement makes false claims when given a private business objective (emergent) or told to deceive (instructed). Multi-round, 8 domains.

**Difference:** the harm is lying about an entitlement, not blocking access to a human. The closest *methodological* template: its emergent/instructed split and knowledge-verification step transfer directly to handoff suppression.

---

## Escalation behaviour (benign, non-adversarial)

- **HiL-Bench / HiL-Dynamics (Scale AI):** whether coding agents ask a human for help on underspecified tasks ("selective escalation"). https://labs.scale.com/blog/hil-dynamics
- **EcoAgent-Bench:** escalating when evidence is insufficient versus avoiding unnecessary escalation under a budget. https://arxiv.org/abs/2608.05519
- **ReliabilityBench:** includes a support domain; agents sometimes close tickets that should be escalated. https://arxiv.org/abs/2601.06112
- **MANTRA:** on τ²-bench, the most common forbidden tool call was premature `transfer_to_human_agents`. https://arxiv.org/abs/2605.06334

**Difference:** all test the agent's own judgement with cooperative users. None tests pressure against the escape path.

---

## Path integrity: say/do gaps

### deadhand777/contact-center, issue #9
https://github.com/deadhand777/contact-center/issues/9

A Bedrock Guardrail refusal message tells the customer a human will take over, but no transfer is triggered and the contact flow keeps looping in the bot. The project's eval could not catch it because it scored contract fields, not agreement between the answer text and the routing those fields produce.

**Relevance:** a clean real-world instance of the false-promise failure (H2).

### "From Confident Closing to Silent Failure" [verify]
https://arxiv.org/abs/2606.09863

Characterises "false success": the agent claims resolution while state is unchanged, on τ²-bench and AppWorld trajectories. Reports that LLM judges struggle to detect it from transcripts.

**Relevance:** the say/do method, applied to task resolution rather than handoff. Supports scoring against system state instead of transcripts.

---

## Vendor testing tools

- **Coval, Transfer & Escalation:** generated scenarios scored against handoff rules, including explicit requests for a human and repeated loops. Cooperative; scored from transcripts. https://www.coval.ai/solutions/agent-behaviors/transfer-escalation/
- **Hamming, Voice Agent Workflow Testing runbook:** recommends treating a handoff as failed if the agent says it transferred but the queue, case, or summary is missing. Guidance, not a benchmark. https://hamming.ai/resources/voice-agent-workflow-testing-runbook

Vendor material is self-reported and commercially motivated.

---

## Operator–user conflict [verify]

- **RealGuardrails / "A Closer Look at System Prompt Robustness":** https://arxiv.org/abs/2502.12197
- **IH-Benchmark:** https://arxiv.org/abs/2607.25987

These reward keeping the system prompt against user override. For Threat A the success criterion inverts: an agent that scores perfectly on these would obey a "never transfer" instruction. This inversion is the basis of H1.

---

## Dark patterns

- **"In Search of Dark Patterns in Chatbots"** (Traubinger et al., CONVERSATIONS 2023). A complaint-based dataset in which some Obstruction cases involve chatbots preventing contact with live agents. Observational, not a test. Dataset: https://github.com/vertr/ChIPS-dataset
- **DarkBench** (ICLR 2025): LLM dark-pattern benchmark. https://arxiv.org/abs/2503.10728. Reportedly does not cover "hard to cancel" obstruction **[verify]**.

---

## Regulation and policy

- **CFPB, "Chatbots in consumer finance" (June 2023):** describes "doom loops", repetitive loops without an offramp to a human representative.
- **California AB 1609, Right to Human Customer Service Act:** good-faith effort to connect a customer to a human within 15 minutes of a request during regular business hours, for businesses above USD 500 million in annual revenue. Presented to the Governor on 14/09/2026. As of 25/09/2026, no signing or veto announcement found; Governor's deadline 30/09/2026. **Check current status** at https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260AB1609
- **EU Directive 2023/2673:** right to request human intervention with fully automated interfaces for distance financial services; applies from 19/06/2026. https://eur-lex.europa.eu/eli/dir/2023/2673/oj/eng
- **Dutch AP and ACM (October 2025):** organisations using chatbots should always offer the option to speak with a person. https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-acm-chatbots-should-not-fully-replace-humans-in-customer-service

**Gap:** rights are tied to business hours or to specific sectors. No compliance tooling measuring time-to-human or reachability was found.

---

## Search limits

Around 40 web searches across the author's own search and a research agent. Security and HCI conference proceedings were not browsed systematically, and private vendor test libraries are not visible. "Not found" means not found under this search, not proof of absence.
