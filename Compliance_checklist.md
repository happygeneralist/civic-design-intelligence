# 🧾 Research Repository Compliance Checklist
*For Local Council / Public Sector User Research Repositories*

---

## 1. Governance & Lawful Basis

- [ ] **Identify lawful basis** for processing (usually *Public Task* under Art 6(1)(e) UK GDPR).  
- [ ] **Check for special category data** (Art 9) — e.g., SEND, health, ethnicity, or child data.  
- [ ] If special category data: ensure condition under **Art 9(2)(j)** (research purpose) and document safeguards.  
- [ ] Conduct or update a **Data Protection Impact Assessment (DPIA)** before repository launch.  
- [ ] Ensure your **Record of Processing Activities (RoPA)** references the repository and linked research workflows.  
- [ ] Appoint a **Data Protection Lead** or confirm with the council’s DPO.

---

## 2. Consent, Transparency & Participant Rights

- [ ] Ensure **Participant Information Sheets** clearly state:  
  - What data is collected (audio, transcript, video, notes).  
  - How long raw data will be kept (e.g., 12 months).  
  - Whether anonymised quotes/insights will be retained long-term.  
  - How participants can withdraw consent or request deletion.  
- [ ] Include a statement that data may be **anonymised for long-term evidence use** in aggregated or public reports.  
- [ ] Keep consent records linked to study IDs (not names).  
- [ ] Make sure withdrawal processes are defined and technically feasible.

---

## 3. Data Minimisation & Anonymisation

- [ ] Remove all identifiers before storing quotes in the repository: names, schools, locations, unique stories.  
- [ ] If anonymisation isn’t feasible, pseudonymise (assign a code instead of identity).  
- [ ] Apply **anonymisation tags** (e.g., `#anon/full`, `#anon/partial`, `#anon/none`) in metadata.  
- [ ] Create and maintain an **Anonymisation Log** explaining transformations.  
- [ ] Ensure anonymisation is irreversible before reuse in reports, decks, or public repositories.

---

## 4. Retention & Deletion Policy

| Data Type | Retention Period | Action |  
|------------|------------------|---------|  
| **Raw data (audio, transcript)** | 12 months (typical) | Delete or archive securely |  
| **Derived quotes (identifiable)** | Until anonymised or consent expires | Redact or anonymise |  
| **Anonymised quotes/insights** | Indefinite (for research/archiving) | Keep under safeguards |  
| **Metadata (study title, date, method)** | Permanent | Keep for audit/history |  

- [ ] Implement a **Retention Schedule** documented in the repository README.  
- [ ] Automate or calendar deletion/archival reviews.  
- [ ] Periodically audit to confirm raw data removal and quote compliance.

---

## 5. Security & Access Control

- [ ] Store repository on **Microsoft-compliant infrastructure** (e.g., GitHub Enterprise, Azure, SharePoint).  
- [ ] Restrict access via **role-based permissions** — only research team & approved analysts.  
- [ ] Enable **encryption at rest and in transit**.  
- [ ] Maintain audit trails (commits, pull requests, issue logs).  
- [ ] Apply security labels (e.g., “OFFICIAL – SENSITIVE”) on all folders/files containing personal data.  
- [ ] Ensure Obsidian local vaults use encrypted drives or OneDrive sync with council account.

---

## 6. Repository Metadata Requirements

Each **Insight / Quote / Study file** must include:

```yaml
lawful_basis: public_task
consent_status: active | expired | not_required
anonymisation_level: full | partial | none
retention_category: raw | quote | anonymised
review_date: YYYY-MM-DD
dpo_contact: dpo@[council].gov.uk
```

---

## 7. Ethical Reuse & Publication

- [ ] Before publishing insights or quotes publicly, confirm:  
  - They are fully anonymised.  
  - No contextual clues could re-identify participants.  
  - Publication aligns with research purpose and council communication policies.  
- [ ] Include attribution note: “This quote has been anonymised and summarises participant views collected under lawful basis for research (Public Task).”  
- [ ] Avoid combining datasets that could indirectly re-identify individuals.  
- [ ] Document reuse decisions and sign-offs.

---

## 8. Review & Continuous Improvement

- [ ] Annual review of DPIA, retention schedule, and anonymisation practices.  
- [ ] Internal audit: randomly sample 5–10 insights per quarter to verify compliance.  
- [ ] Capture lessons learned (e.g., anonymisation challenges, data handling improvements).  
- [ ] Publish a brief **Transparency Statement** describing repository governance.
