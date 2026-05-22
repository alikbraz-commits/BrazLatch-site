# Reply template — fallback / closed-market / off-topic

Use this template **only** when the inquiry doesn't fit AU/NZ, UK/EU, or
India — i.e. they're from a market that's already covered or out of scope:

- **United States, Canada, established Europe (DE/FR/NL/BE/DK/SE/NO/FI):**
  redirect to existing distribution channels.
- **Other / unclear:** acknowledge and ask Alik before committing.

---

## US / Canada / established EU — redirect template

**Subject:** Re: BrazLatch enquiry — distribution in {{country}}

Hi {{first_name}},

Thanks for writing. BrazLatch is already on shelves in {{country}}:

{{channels_for_their_market}}

If you're a retail buyer at one of those chains, the right path is to
contact them directly. If you're after stock for resale, those four
already hold our distribution there.

For genuinely unusual requirements — large institutional orders,
custom OEM applications, or a vertical we don't cover today — write
back and tell me a bit more about what you're trying to do. I'm happy
to look.

Alik

---

**`{{channels_for_their_market}}` content:**

- **USA:** "BrazLatch is sold through National Hardware (the major US
  hardware distribution channel), Lowe's stores, and Amazon US."
- **Canada:** "BrazLatch is distributed in Canada through Ajustco
  (ajustco.com) and is available on Amazon Canada."
- **Germany / France / Netherlands / Belgium / Denmark / Sweden / Norway / Finland:**
  "BrazLatch is distributed in your market through Ajustco — ajustco.com
  for direct contact."

---

## Unclear / off-topic — flag-to-Alik template

If the inquiry is clearly not a distributor enquiry (consumer
complaint, journalist, recruiter, supplier pitch, vendor spam), **do
not draft a public reply.** Instead:

1. Add the inquiry to `pipeline.json` with `status: passed` and
   `score: 0`.
2. Note the reason in `notes`.
3. Surface it to Alik with: "Inquiry #{{id}} doesn't look like a
   distributor lead — looks like {{reason}}. Reply or ignore?"
4. Wait for Alik's call.
