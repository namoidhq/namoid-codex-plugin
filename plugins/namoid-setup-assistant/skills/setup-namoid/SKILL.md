---
name: setup-namoid
description: Configure, diagnose, or repair NamoID Customer Identity integrations. Use when a user asks Codex to add NamoID authentication, inspect an existing integration, configure callbacks or applications, troubleshoot sign-in, or verify readiness.
---

# Set up NamoID

1. Inspect the repository before proposing changes. Identify the framework,
   package manager, NamoID SDK, callback route, application origin, and relevant
   environment-variable names without reading or revealing secret values.
2. Use the NamoID Setup Assistant MCP for authoritative remote state. Begin
   with `setup.read`; use `setup.write` only when the user requests a mutation.
3. Default to Test. Require explicit confirmation for every Live mutation.
4. Preview local and remote changes together, then apply only approved work.
5. Run focused checks and identify any Console-only actions.

Never put secrets, tokens, OTPs, or private keys in model context. Never create
or rotate application secrets. Do not guess among multiple NamoID resources,
and do not treat MCP access as permission to modify local files.
