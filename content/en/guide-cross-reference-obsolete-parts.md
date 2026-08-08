<!--
PAGE TYPE : Guide / Cross-reference (top-of-funnel authority + capture)
URL SLUG  : /en/guides/cross-reference-obsolete-parts/
TARGET KW : cross reference obsolete parts | how to find replacement for discontinued part | industrial part cross reference
INTENT    : Informational → commercial (engineer figuring out how to replace a discontinued part)
STATUS    : Ready to publish.
-->

TITLE TAG      : How to Cross-Reference an Obsolete Automation Part (2026 Guide)
META DESC (154): A step-by-step way to find the right replacement for a discontinued industrial part — from decoding the model number to verifying certification and authenticity.
H1             : How to Cross-Reference an Obsolete Automation Part

---

## The problem

A part is discontinued and you need "the new equivalent." But swapping the wrong replacement into a running process can mean a bad measurement, a failed loop, or a certification gap on a safety point. Cross-referencing done properly is a short checklist — here it is.

---

## Step 1 — Capture the full identity of the old part

Don't work from memory. From the tag, record:

- **Full model / catalog number** (every character — option codes matter).
- **Serial number** (tells the OEM the exact build).
- **Range and units** (for transmitters/gauges).
- **Output / protocol** (4–20 mA, HART, digital bus).
- **Certification** (SIL rating, Ex/ATEX zone, IP rating).
- **Process connection & mounting** (thread, flange, footprint).

> The option code is where most cross-references go wrong. Two units with the "same" base model can differ in range, wetted materials or certification.

---

## Step 2 — Find the OEM-designated successor first

Manufacturers usually name a successor when they retire a product (e.g. Rosemount 1151 → 3051; Mitsubishi FX3U → FX5U; Allen-Bradley PLC-5 → ControlLogix). Start there — it's the best-supported path, even if it isn't a mechanical drop-in.

If the successor isn't a drop-in, decide whether you can accept:
- **Wiring / footprint changes** (common on PLC and transmitter upgrades), or
- A **form-fit-function drop-in** from a third party (keeps the same mounting/wiring).

---

## Step 3 — Match the specs that actually matter

Line up old vs candidate on the points that affect the process:

| Check | Why it matters |
|---|---|
| Range / span & rangedown | Wrong range = poor accuracy or out-of-range |
| Accuracy & stability | Must meet or beat the loop's requirement |
| Output / protocol | Must match the control system input |
| Certification (SIL, Ex/ATEX, IP) | A gap here can be a safety/compliance failure |
| Process connection & materials | Must suit the fluid, pressure and mounting |
| Power / signal | Loop-powered vs externally powered, voltage |

**A cross-reference that matches the model number but not the certification is not a valid replacement for a safety point.**

---

## Step 4 — Verify authenticity before it goes on the machine

Especially for popular legacy parts (heavily counterfeited), confirm the replacement is genuine: buy through a source that provides **functional testing and traceability**, not an anonymous marketplace listing. A fake that passes a bench test can still fail in service.

---

## Step 5 — Document the change

Record the old part, the chosen replacement, the spec comparison, and "verified against OEM datasheet on <date>." Future-you (and your auditor) will need it.

---

## Worked cross-references

- [Rosemount 1151 → 3051 / drop-in](/en/obsolete/rosemount-1151-replacement/)
- [Mitsubishi FX3U → FX5U](/en/obsolete/mitsubishi-fx3u-replacement-fx5u/)
- [Allen-Bradley PLC-5 / SLC 500 → ControlLogix / CompactLogix](/en/obsolete/allen-bradley-plc5-slc500-replacement/)

---

## Let us cross-reference it for you

Send the **model/serial from the tag** and we'll return the OEM successor, any qualified drop-in, and current sourcing options — with certification matched and authenticity verified.

**→ [Request a cross-reference & quote](/en/sourcing/)**

---

## FAQ

**How do I find the replacement for a discontinued industrial part?**
Capture the full model/serial and specs, find the OEM-designated successor, match range/output/certification/connection, then verify authenticity before fitting. Or send us the number and we'll cross-reference it.

**Is the successor always a drop-in?**
No. Many successors change wiring or footprint. If you need the exact same mounting and wiring, use a form-fit-function drop-in instead.

**Why is certification part of a cross-reference?**
Because a part that matches the model number but not the SIL/Ex/ATEX rating isn't a valid replacement on a safety or hazardous-area point.

<!-- SCHEMA TO ADD: HowTo (Steps 1-5) + FAQPage + BreadcrumbList.
     INTERNAL LINKS OUT: all /en/obsolete/* pages, /en/services/obsolete-parts-sourcing/, /en/services/counterfeit-screening/. -->
