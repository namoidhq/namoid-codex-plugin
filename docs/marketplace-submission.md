# Official marketplace submission

This file is the reviewer-ready source of truth for the NamoID Customer Identity
public listing. Do not include production credentials or customer data in a
submission.

## Listing

- **Name:** NamoID Customer Identity
- **Publisher:** NamoID / PolyMindsLabs Pvt. Ltd.
- **Category:** Developer Tools
- **Website:** https://namoid.in
- **Documentation:** https://docs.namoid.in
- **Support:** https://github.com/namoidhq/namoid-codex-plugin/issues
- **Privacy policy:** https://namoid.in/privacy
- **Terms:** https://namoid.in/terms
- **MCP server:** https://mcp.namoid.in
- **Logo asset:** `web/public/brand/namoid-avatar-1024.png` in the NamoID
  application repository
- **Brand color:** `#0B664F`

### Short description

Set up, diagnose, and review NamoID Customer Identity integrations.

### Long description

NamoID Customer Identity helps developers connect an application to NamoID
Customer Identity, register exact OAuth callback and logout URLs, inspect hosted
authentication configuration, diagnose common integration errors, and run
production-readiness checks. It combines guided skills with the scoped NamoID
Setup Assistant MCP. Browser-based OAuth keeps access attributable and
revocable. The server never returns client-secret values.

### Release notes

Version 0.2.0 adds six Customer Identity workflows for setup, diagnosis,
verification, logout, session security, and production readiness; uses the
canonical production MCP endpoint; and improves marketplace metadata and
reviewer documentation.

## Authentication and data access

The MCP uses OAuth Authorization Code with S256 PKCE and the production
authorization server at `https://auth.namoid.in`. Its protected-resource
metadata is available at
`https://mcp.namoid.in/.well-known/oauth-protected-resource`.

Requested resource scopes:

- `customer-identity:read`: inspect accessible workspaces, projects,
  environments, applications, hosted-auth configuration, and readiness.
- `customer-identity:configure`: update configuration in explicitly selected Customer
  Identity configuration. This is requested only when write access is needed.
NamoID processes the signed-in user's account identifier and the configuration
needed to perform a requested setup operation. Tool responses may contain
workspace, project, environment, and application identifiers and public OAuth
Client IDs. They do not contain passwords, access tokens, refresh tokens, client
secrets, private signing keys, or provider tokens.

## Starter prompts

1. Set up NamoID authentication for this application.
2. Diagnose why this application's NamoID callback is failing.
3. Review this NamoID integration for production readiness.
4. Check whether logout and session handling are implemented safely.
5. Show the current NamoID applications and callback URLs without making changes.

## Positive test cases

1. **Read-only discovery:** Ask to list accessible NamoID workspaces. The plugin
   authenticates the user, requests read access, and returns only authorized
   workspaces.
2. **Application setup:** In an authorized Test environment, ask to create a
   public SPA application with one exact HTTPS callback. The plugin confirms the
   requested values, creates the application, and returns its public Client ID
   without any secret.
3. **Callback diagnosis:** Provide a callback-mismatch error and ask for help.
   The plugin inspects registered callbacks, explains the mismatch, and does not
   modify configuration unless explicitly asked.
4. **Production readiness:** Ask for a launch-readiness review. The plugin runs
   read-only checks and reports blockers with remediation.
5. **Idempotent update:** Ask to add a callback that is already registered. The
   plugin reports no effective change and does not create a duplicate.

## Negative test cases

1. **Unauthorized tenant:** Ask to inspect a workspace the signed-in user cannot
   access. The server denies the request without revealing workspace metadata.
2. **Secret retrieval:** Ask for an application's client secret, access token,
   refresh token, or signing key. The plugin explains that secret values are not
   retrievable and does not expose them.
3. **Unconfirmed mutation:** Ask vaguely to “fix everything” without identifying
   the target or approving changes. The plugin inspects safely, proposes exact
   changes, and does not mutate remote configuration.

## Tool review

All tools publish `readOnlyHint`, `destructiveHint`, `idempotentHint`, and
`openWorldHint`. Read tools set `readOnlyHint: true`; create and update tools
set it to `false`. No exposed tool deletes resources, so
`destructiveHint` is `false`. Operations are limited to NamoID and therefore
use `openWorldHint: false`.

Before submission, scan the production MCP in the marketplace portal and review
the generated schemas and annotations. Use a dedicated reviewer account with
Test-only sample data. Never provide access to a real customer workspace.
