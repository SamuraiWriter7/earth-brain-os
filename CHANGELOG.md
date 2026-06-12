# Changelog

All notable changes to this project will be documented in this file.

This project follows a draft-oriented specification lifecycle.

---

## [v0.1.0-candidate] - 2026-06-13

### Added

* Added `docs/earth-brain-os-architecture.md`, defining **Earth Brain OS Architecture** as a civilizational reference model for AI agents, optical networks, knowledge archives, trace records, attribution, royalty circulation, Kazene-style distributed regulation, defense layers, and human governance.

* Added `schemas/earth-brain-event.schema.json`, defining the minimal **Earth Brain Event** schema for recording integrated flows across:

  * AI Agent Layer
  * Optical Nervous Layer
  * Knowledge Cortex Layer
  * Trace and Attribution Layer
  * Royalty Circulation Layer
  * Kazene Regulation Layer
  * Defense and Immune Layer
  * Human Governance Layer

* Added `examples/earth-brain-os-flow.example.yaml`, providing a minimal integrated Earth Brain OS flow example involving:

  * AI-assisted OSS contribution
  * Knowledge source usage
  * Trace and attribution record
  * Kazene pressure regulation
  * Defense monitoring
  * Human governance review
  * Royalty and value circulation routing

* Added `scripts/validate_examples.py`, a validation script for checking YAML examples against JSON Schemas.

* Added explicit validation mapping for `earth-brain-os-flow.example.yaml` to `earth-brain-event.schema.json`.

* Added `.github/workflows/validate-examples.yml`, enabling automated GitHub Actions validation for schemas, examples, and validation script changes.

* Added repository-level structure for:

  * `docs/`
  * `schemas/`
  * `examples/`
  * `scripts/`
  * `.github/workflows/`

### Defined

* Defined Earth Brain OS as a civilizational reference architecture connecting:

  * AI agents as distributed neurons
  * Optical networks as nervous fibers
  * Knowledge archives as civilizational cortex
  * Trace records as memory
  * Royalty circulation as value reinforcement
  * Kazene regulation as breathing and pressure control
  * Defense layers as immune response
  * Human governance as reflective consciousness

* Defined the initial Earth Brain OS layer model:

```text
Earth Brain OS
├─ 1. AI Agent Layer
├─ 2. Optical Nervous Layer
├─ 3. Knowledge Cortex Layer
├─ 4. Trace and Attribution Layer
├─ 5. Royalty Circulation Layer
├─ 6. Kazene Regulation Layer
├─ 7. Defense and Immune Layer
└─ 8. Human Governance Layer
```

* Defined the initial Earth Brain OS lifecycle:

```text
1. contribution_created
2. source_detected
3. agent_involvement_recorded
4. trace_generated
5. attribution_route_created
6. pressure_level_evaluated
7. trust_route_assigned
8. review_completed
9. royalty_route_generated
10. value_returned
11. feedback_recorded
```

### Validation

* Confirmed that Earth Brain OS examples can be validated against JSON Schemas using:

```bash
python scripts/validate_examples.py
```

* Added automated validation through GitHub Actions.

### Notes

* This release establishes the first minimal working structure of Earth Brain OS.
* The repository now includes architecture documentation, machine-readable schema, YAML example, local validation, and CI validation.
* This version is suitable for tagging as `v0.1.0-candidate`.

---

## [Unreleased]

### Planned

* Add `schemas/kazene-regulation-event.schema.json`.
* Add `examples/kazene-regulation-event.example.yaml`.
* Add `schemas/agentic-contribution-pressure.schema.json`.
* Add `examples/agentic-contribution-pressure.example.yaml`.
* Add `schemas/royalty-circulation-event.schema.json`.
* Add `examples/royalty-circulation-event.example.yaml`.
* Add `schemas/human-governance-review.schema.json`.
* Add `examples/human-governance-review.example.yaml`.
* Expand validation coverage for future Earth Brain OS sub-events.
* Add relationship documentation for Royalty OS, Trace Protocol, Q-Point Protocol, Defense Court Protocol, and Kazene Regulation Layer.
