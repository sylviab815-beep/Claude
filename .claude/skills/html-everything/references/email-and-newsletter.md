# Email and Newsletter HTML

Email-safe HTML for newsletter platforms (Substack, ConvertKit, MailerLite, Mailchimp) and for direct pasting into Substack post editors.

## When to use

- "Make me a newsletter template"
- "Build a Substack post for [X]"
- "Email blast for the audiobook release"
- "Welcome email for new subscribers"
- "Email-safe HTML for [event]"

## The email-safe constraint

Email clients (Gmail, Outlook, Apple Mail) strip or break modern CSS. Email-safe HTML is much more limited than web HTML:

- **No `<style>` blocks** — most clients strip them. Use inline `style="..."` on every element.
- **No `<link>` to external CSS** — same reason.
- **No CSS Grid or Flexbox** — Outlook eats them. Use HTML `<table>` for layout.
- **No `@media` queries** — limited support. Build for mobile-first widths.
- **No external fonts** — Google Fonts won't load. Use email-safe stacks.
- **No JavaScript** — every client strips it.
- **No background images via CSS** — use `<img>` tags or solid `bgcolor` attributes.
- **No `box-shadow`, `border-radius` beyond simple** — partial support.
- **Width: 600px max** for the main container — standard email convention.

Substack is the friendliest. ConvertKit and MailerLite are stricter. Direct email blasts (raw SMTP, hand-pasted) are the strictest.

## Email-safe font stacks

- **Serif:** `Georgia, 'Times New Roman', serif`
- **Sans-serif:** `Arial, Helvetica, sans-serif`
- **Monospace:** `'Courier New', monospace`

Don't try to use Iowan Old Style, Palatino, or any system font in email — fallbacks will trigger inconsistently.

## Starter HTML — Substack-paste-ready

Substack's editor accepts more HTML than raw email, but pasting from VS Code or a browser often strips things. The safest approach:

```html
<div style="max-width: 580px; margin: 0 auto; font-family: Georgia, 'Times New Roman', serif; font-size: 17px; line-height: 1.65; color: #1a1a1a;">

<h1 style="font-size: 28px; margin: 0 0 24px; font-weight: 600; color: #1a1a1a;">[POST TITLE]</h1>

<p style="margin: 0 0 1em;">[Opening paragraph.]</p>

<p style="margin: 0 0 1em;">[Next paragraph.]</p>

<hr style="border: 0; border-top: 1px solid #d4cfc5; margin: 36px auto; max-width: 80px;">

<p style="margin: 0 0 1em; font-style: italic; color: #6a6a6a; font-size: 15px;">[A small subhead or italicized aside.]</p>

<p style="margin: 0 0 1em;">[Continue body text.]</p>

<p style="margin: 32px 0 1em;">— Kate</p>

</div>
```

Notes for Substack:
- Substack's editor often re-wraps your HTML when you paste. Test with a small section first.
- Block quotes work: `<blockquote style="border-left: 3px solid #5a2a2a; padding-left: 16px; font-style: italic; margin: 24px 0;">`.
- Images: upload through Substack's image button, not via `<img>` — Substack hosts them.
- Buttons: Substack has a button block; don't try to inline-style one.
- Links: standard `<a href="...">` works.

## Starter HTML — email blast (table-based, maximum compatibility)

For raw email sends (not Substack), use table layout. This is the most defensively-coded email HTML:

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[EMAIL SUBJECT]</title>
</head>
<body style="margin: 0; padding: 0; background-color: #faf8f4; font-family: Georgia, 'Times New Roman', serif;">

<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #faf8f4;">
  <tr>
    <td align="center" style="padding: 32px 16px;">

      <!-- Main container -->
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="max-width: 600px; background-color: #ffffff; border: 1px solid #e4dfd5;">

        <!-- Header -->
        <tr>
          <td align="center" style="padding: 32px 24px 8px;">
            <h1 style="margin: 0; font-family: Georgia, serif; font-size: 28px; color: #1a1a1a; letter-spacing: 0.02em;">
              [EMAIL HEADER]
            </h1>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td style="padding: 16px 32px 32px; font-family: Georgia, serif; font-size: 17px; line-height: 1.65; color: #1a1a1a;">
            <p style="margin: 0 0 1em;">[Opening paragraph.]</p>
            <p style="margin: 0 0 1em;">[Body paragraph.]</p>
            <p style="margin: 0 0 1em;">[Body paragraph.]</p>
          </td>
        </tr>

        <!-- CTA button -->
        <tr>
          <td align="center" style="padding: 16px 32px 32px;">
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td bgcolor="#1a1a1a" style="border-radius: 2px;">
                  <a href="[CTA_URL]" style="display: inline-block; padding: 14px 28px; font-family: Arial, sans-serif; font-size: 15px; letter-spacing: 0.06em; color: #faf8f4; text-decoration: none;">
                    [BUTTON TEXT]
                  </a>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Sign-off -->
        <tr>
          <td style="padding: 16px 32px 32px; font-family: Georgia, serif; font-size: 17px; line-height: 1.65; color: #1a1a1a;">
            <p style="margin: 0;">— Kate</p>
          </td>
        </tr>

      </table>

      <!-- Footer / unsubscribe -->
      <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="max-width: 600px;">
        <tr>
          <td align="center" style="padding: 24px 16px; font-family: Arial, sans-serif; font-size: 12px; color: #6a6a6a;">
            <p style="margin: 0 0 8px;">You're receiving this because you signed up for [LIST NAME].</p>
            <p style="margin: 0;"><a href="[UNSUBSCRIBE_URL]" style="color: #6a6a6a;">Unsubscribe</a></p>
          </td>
        </tr>
      </table>

    </td>
  </tr>
</table>

</body>
</html>
```

## Common email scenarios

**Audiobook release blast:** Subject line as the hook. Top: cover or audiobook poster. Body: 2-3 short paragraphs of why this narrator/why audio. CTA: Listen now → Audible. Sign-off personal. Footer: unsubscribe + list info.

**New release announcement:** Same shape, with retailer buttons (multiple) in the CTA block. Each retailer is its own button row in the table.

**Welcome email:** Warmer. Personal greeting. One-paragraph "what to expect from this newsletter." A small gift (free chapter, deleted scene, character map link). CTA optional — sometimes a welcome email is just relationship-building.

**Substack post promoting a release:** More conversational than email blast. Lead with a hook line or quote. Tell the story of WHY this book matters. Drop retailer links inline. Cover image. Sign-off.

## Pre-flight email checklist

Before delivering:

- [ ] All styles inline (no `<style>` block)
- [ ] Layout is `<table>`-based (not flexbox/grid)
- [ ] Max width 600px on main container
- [ ] Fonts are email-safe stacks (Georgia, Arial, Times)
- [ ] No JavaScript
- [ ] No external CSS files
- [ ] Images have `alt` attributes
- [ ] CTA buttons are `<table>`-wrapped `<a>` tags (Outlook needs this)
- [ ] Unsubscribe link present if it's a list send
- [ ] Subject line / preview text decided
