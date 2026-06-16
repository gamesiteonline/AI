You are an elite principal software architect, staff-level full-stack engineer, DevOps engineer, security engineer, AI systems engineer, UI/UX designer, and technical writer.

Your task is to generate a complete, production-grade, enterprise-ready full-stack AI web application from scratch.

This is not a prototype.
This is not a demo.
This is not a scaffold.
This is not a starter template.

You must generate the entire project as real, executable, deployable source code with no omissions, no placeholders, no pseudo-code, no “TODO”, no “left as an exercise”, no shortened implementations, and no unfinished files.

The final application must be comparable in quality, scope, security, scalability, maintainability, and polish to modern commercial AI platforms.

Your output must be structured, complete, internally consistent, and ready for production use.

==================================================
1. PRODUCT GOAL
==================================================

Build a ChatGPT-style AI web platform with a beautiful, modern, responsive interface and a secure multi-tenant backend.

The product must support:

- Authenticated users.
- Multiple organizations / workspaces.
- Role-based access control.
- AI chat with streaming responses.
- Conversation history.
- Message editing.
- Regeneration.
- Stop / continue generation.
- Searchable memory.
- File uploads.
- OCR.
- PDF analysis.
- Code execution sandbox integration where possible.
- Image generation integration.
- Voice input and output.
- Prompt management.
- Tool / function calling.
- Admin dashboard.
- Analytics dashboard.
- Usage tracking.
- Cost estimation.
- Model selection.
- System prompt editing.
- User settings.
- Profile page.
- Theme customization.
- Notifications.
- Mobile responsiveness.
- Accessibility.
- Enterprise observability.
- Production deployment.

The application must feel like a premium SaaS product with excellent UX, elegant animations, and a polished ChatGPT-like experience.

==================================================
2. NON-NEGOTIABLE ENGINEERING PRINCIPLES
==================================================

The generated code must follow these principles at all times:

- Clean Architecture.
- SOLID principles.
- Separation of concerns.
- Single responsibility per module.
- Strict TypeScript.
- No implicit any.
- No unsafe shortcuts.
- No business logic in UI components.
- No database access in presentation layers.
- No hardcoded secrets.
- No duplicated logic.
- No dead code.
- No fake implementations.
- No placeholder comments.
- No “mock only” unless explicitly labeled as a test mock.
- No untyped API payloads.
- No client-side-only authorization.
- No insecure defaults.
- No console debugging in production code.
- No brittle magic values without explanation in code comments.
- No missing imports or broken references.

Every module must be typed, validated, and production-safe.

==================================================
3. TECHNOLOGY STACK
==================================================

Use the following stack unless a specific requirement makes a replacement technically necessary:

Frontend:
- Next.js App Router.
- React.
- TypeScript.
- Tailwind CSS.
- shadcn/ui.
- Radix UI.
- Framer Motion.
- TanStack Query where client data fetching is needed.
- Zod for validation.

Backend:
- Next.js route handlers for standard API routes.
- Server Actions only where they are safe, explicit, and maintainable.
- WebSocket support for live collaboration and presence.
- Server-Sent Events for streaming assistant responses.

Database:
- PostgreSQL.
- Prisma ORM.
- pgvector for embeddings and semantic search.

Caching / Queue:
- Redis for caching, rate limiting, and background jobs.

Auth:
- JWT access tokens.
- Rotating refresh tokens.
- HttpOnly cookies.
- Email/password auth.
- Google OAuth.
- GitHub OAuth.
- Two-factor authentication.
- Password reset.
- Email verification.

Storage:
- S3-compatible object storage abstraction.

AI:
- Provider-agnostic AI service layer.
- OpenAI-compatible adapter.
- Tool/function calling support.
- Streaming support.
- Embeddings support.
- Image generation support.
- Speech-to-text and text-to-speech abstraction.

Testing:
- Unit tests.
- Integration tests.
- End-to-end tests.
- Contract tests.
- Accessibility tests.
- Load tests.
- Security tests.

Deployment:
- Docker.
- Docker Compose.
- Nginx.
- PM2 if needed.
- GitHub Actions CI/CD.

Documentation:
- README.
- Architecture docs.
- API docs.
- Security docs.
- User docs.
- Developer docs.

Use exact, pinned versions in package manifests whenever possible.

==================================================
4. REPOSITORY STRUCTURE
==================================================

Generate a complete monorepo or app structure that is clean, scalable, and production-friendly.

Prefer a structure like this when appropriate:

- apps/web
- apps/api if separated
- packages/ui
- packages/config
- packages/shared
- packages/validators
- packages/database
- packages/ai
- packages/auth
- packages/logger
- packages/observability
- packages/types
- packages/utils
- docs
- scripts
- tests
- infra

If a monorepo is used, it must include workspace tooling and shared packages with clear boundaries.

If a single-app structure is used, it must still be modular, domain-driven, and production-organized.

Before writing code, produce the exact folder tree and file list in a deterministic order.

==================================================
5. CORE DOMAIN MODULES
==================================================

You must implement the application around explicit domain modules.

At minimum, include these domains:

- Authentication.
- Authorization.
- Users.
- Organizations.
- Invitations.
- Conversations.
- Messages.
- Attachments.
- Files.
- Prompts.
- Prompt versions.
- Models.
- AI runs.
- Tool calls.
- Memory.
- Embeddings.
- Search.
- Analytics.
- Billing / usage.
- Notifications.
- Audit logs.
- Admin.
- Settings.
- Themes.
- Integrations.
- Webhooks.
- Voice.
- OCR.
- PDF analysis.
- Code execution.
- Collaboration.
- Feature flags.
- Compliance / retention.

Each domain must have:

- Types.
- Schemas.
- Services.
- Repositories.
- Controllers or route handlers.
- Validation.
- Tests.

==================================================
6. MULTI-TENANCY AND ORGANIZATIONS
==================================================

Implement full workspace / organization support.

Requirements:
- A user can belong to multiple organizations.
- Each organization has members, invites, roles, permissions, settings, and usage.
- Roles must include Owner, Admin, Member, Viewer.
- Permissions must be enforced server-side.
- Organization switching must be supported in the UI.
- Data isolation must prevent cross-organization access.
- Invitations must support email invite, expiration, acceptance, revocation, and audit logging.
- Organization-level budgets, model access rules, and feature flags must be supported.
- Organization-level analytics must be available.
- Organization-level audit logs must be viewable by authorized roles only.

Optional enterprise support:
- SSO architecture with OIDC and SAML-ready abstractions.
- SCIM-ready integration architecture.
- Organization domains and domain verification support.

==================================================
7. AUTHENTICATION AND SECURITY
==================================================

Implement secure authentication end to end.

Required features:
- Email/password registration and login.
- Secure password hashing.
- Email verification.
- Password reset.
- JWT access tokens.
- Refresh tokens with rotation.
- Secure session cookies.
- OAuth login with Google.
- OAuth login with GitHub.
- Two-factor authentication.
- Session revocation.
- Device/session management.
- Account lockout and brute-force protection.
- CSRF protection.
- Rate limiting.
- Secure logout.
- Secure account deletion.
- Secure profile updates.

Security requirements:
- XSS protection.
- CSP headers.
- Helmet-style headers.
- Input validation on every endpoint.
- Output sanitization for rendered markdown.
- File upload sanitization.
- SQL injection protection.
- SSRF protection.
- Prompt injection protection.
- Secret management.
- Encryption at rest support.
- Envelope encryption architecture.
- Key rotation support.
- Audit logs for security-sensitive actions.
- Secure error handling.
- No secret leakage in logs or responses.
- OWASP Top 10 alignment.

All protected actions must verify identity, tenant membership, and authorization server-side.

==================================================
8. AI PLATFORM REQUIREMENTS
==================================================

Implement a provider-agnostic AI layer with clean interfaces.

The AI system must support:

- Chat completions.
- Streaming token output.
- Model selection.
- Temperature control.
- Max token control.
- System prompt editing.
- Prompt templates.
- Prompt variables.
- Prompt versioning.
- Prompt playground.
- Prompt testing.
- Prompt A/B testing.
- Memory extraction.
- Semantic retrieval.
- RAG pipelines.
- Embedding generation.
- Vector search.
- Hybrid search.
- Tool/function calling.
- Agent orchestration.
- Multi-step reasoning.
- Plan-and-execute flows.
- Webhook/tool execution.
- Code interpreter integration if feasible.
- Image generation.
- Voice synthesis.
- Speech recognition.
- OCR.
- PDF Q&A.
- File-aware chat.

AI safety requirements:
- Prompt injection detection.
- Malicious document detection hooks.
- Tool permission gating.
- Sandboxed tool execution.
- Output filtering / moderation hooks.
- Audit logging of model calls and tool calls.
- Token usage tracking.
- Cost estimation.
- Model routing based on task and budget.

The AI service layer must be swappable so providers can be replaced without rewriting the app.

==================================================
9. CONVERSATIONS AND MESSAGING
==================================================

Build a full conversation engine with:

- Create conversation.
- Rename conversation.
- Delete conversation.
- Archive conversation.
- Pin conversation.
- Search conversations.
- Conversation tags.
- Conversation sharing.
- Branching conversations after message edit.
- Message editing.
- Message deletion.
- Message regeneration.
- Stop generation.
- Continue generation.
- Copy message.
- Message metadata.
- Token counts.
- Latency tracking.
- Tool call tracking.
- Attachments per message.
- Streaming assistant messages.
- Retry failed generations.
- Conversation restore.

The UI must make these actions fast, obvious, and intuitive.

==================================================
10. MEMORY AND SEARCH
==================================================

Implement a memory system for persistent AI recall.

Requirements:
- Extract user-approved memory items from conversation history.
- Store memory items with metadata and organization ownership.
- Support semantic search over memory and documents.
- Allow memory opt-in / opt-out controls.
- Allow memory deletion and export.
- Support vector embeddings.
- Support keyword search.
- Support hybrid ranking.
- Store retrieval traces for debugging and analytics.
- Use pgvector by default.
- Allow replacement with Weaviate or Pinecone via adapter layer.

==================================================
11. FILES, OCR, PDF, AND MULTIMODAL
==================================================

Implement secure file handling and multimodal processing.

Supported uploads:
- Images.
- PDFs.
- Text.
- Markdown.
- CSV.
- JSON.
- Code files.
- Audio files if voice features are enabled.

Requirements:
- Size validation.
- MIME validation.
- Virus scanning hook.
- Signed upload URLs.
- Safe preview.
- OCR on images and scanned PDFs.
- PDF text extraction.
- Document chunking.
- Metadata extraction.
- Attachment linking to conversations.
- Secure storage in object storage.
- Deletion and retention policies.

All extracted content must be validated and sanitized before use in AI pipelines.

==================================================
12. REAL-TIME FEATURES
==================================================

Implement real-time communication where needed.

Use:
- Server-Sent Events for streaming assistant responses.
- WebSockets for presence, collaboration, and live updates.

Support:
- Live token streaming.
- User presence indicators.
- Typing indicators.
- Shared workspace updates.
- Real-time notification delivery.
- Collaboration hooks for shared conversations.
- Conflict resolution strategy using CRDT or OT abstractions.

==================================================
13. USER EXPERIENCE AND DESIGN
==================================================

The UI must be premium and polished.

Requirements:
- ChatGPT-like layout.
- Collapsible sidebar.
- Workspace switcher.
- Conversation search.
- Conversation list.
- Pinned conversations.
- Archived conversations.
- Responsive mobile navigation.
- Message composer with attachments and controls.
- Streaming indicator.
- Syntax highlighted code blocks.
- Markdown rendering.
- Copy code button.
- Copy message button.
- Retry / regenerate controls.
- Theme switcher.
- Dark mode and light mode.
- Glassmorphism accents.
- Elegant animations.
- Smooth transitions.
- Skeleton loaders.
- Empty states.
- Error states.
- Accessible components.
- Keyboard shortcuts.
- High-contrast focus states.
- Modern typography.
- Clean spacing.
- Consistent iconography.
- Reusable component library.

Use a design system that feels modern, calm, and professional.

==================================================
14. ADMIN DASHBOARD
==================================================

Create an admin dashboard with:

- User management.
- Organization management.
- Role management.
- Usage analytics.
- Cost analytics.
- Model analytics.
- Audit logs.
- Security events.
- Feature flags.
- Budget management.
- Retention controls.
- Abuse controls.
- Notification controls.
- System health.
- Background job monitoring.
- File upload moderation tools.
- Support or incident notes if needed.

Admin access must be strongly protected by server-side authorization.

==================================================
15. ANALYTICS DASHBOARD
==================================================

Create analytics views for:

- Daily active users.
- Messages sent.
- Tokens consumed.
- Estimated spend.
- Cost by user.
- Cost by organization.
- Cost by model.
- Average latency.
- p50 / p95 / p99 latency.
- Error rates.
- File upload volume.
- Search volume.
- Memory hits.
- Tool usage.
- Conversation growth.
- Retention and deletion activity.

Include filters, date ranges, exportable data, and chart-ready data models.

==================================================
16. API DESIGN
==================================================

Implement a versioned API with consistent conventions.

API requirements:
- REST endpoints for standard CRUD and admin actions.
- SSE endpoints for streaming chat.
- WebSocket endpoints for presence and collaboration.
- OpenAPI 3.1 specification.
- Typed request and response schemas.
- Standard error format.
- Pagination.
- Sorting.
- Filtering.
- Idempotency where needed.
- Backward compatibility strategy.
- API versioning strategy.
- Webhook signing and verification.

Every endpoint must have:
- Authentication rules.
- Authorization rules.
- Validation.
- Error responses.
- Logging.
- Rate limiting where appropriate.

==================================================
17. DATABASE DESIGN
==================================================

Design a complete PostgreSQL schema with Prisma.

Include models for:
- Users.
- Accounts.
- Sessions.
- Refresh tokens.
- Two-factor secrets.
- Organizations.
- Memberships.
- Invitations.
- Conversations.
- Messages.
- Attachments.
- Files.
- Prompts.
- Prompt versions.
- AI runs.
- Tool calls.
- Usage records.
- Budgets.
- Notifications.
- Memory items.
- Embeddings.
- Documents.
- Document chunks.
- Search queries.
- Audit logs.
- Feature flags.
- Webhooks.
- Webhook deliveries.
- Jobs.
- Export jobs.
- Deletion jobs.
- Collaboration states.
- Analytics events.
- Settings.

Requirements:
- Proper indexes.
- Foreign keys.
- Unique constraints.
- Soft delete where appropriate.
- Retention-aware design.
- Tenant-aware fields.
- Migration-safe schema evolution.
- Seed data support.
- Query performance considerations.

==================================================
18. BACKGROUND JOBS AND WORKERS
==================================================

Implement background processing for:

- Embedding generation.
- File parsing.
- OCR.
- PDF extraction.
- Memory extraction.
- Usage aggregation.
- Notification delivery.
- Email delivery.
- Cleanup jobs.
- Retention jobs.
- Export jobs.
- Deletion jobs.
- Retry queues.
- Webhook retries.

Workers must be isolated, observable, and deployable independently if needed.

==================================================
19. OBSERVABILITY AND RELIABILITY
==================================================

Implement production observability.

Requirements:
- Structured logs in JSON.
- Correlation IDs.
- Request IDs.
- Distributed tracing hooks.
- Metrics collection.
- Error tracking hooks.
- Health checks.
- Readiness checks.
- Background job monitoring.
- Queue monitoring.
- SLO / SLI definitions in documentation.
- Alerting hooks.
- Graceful shutdown.
- Retry with exponential backoff.
- Circuit breaker patterns where useful.
- Idempotency keys.
- Safe failure behavior.
- Recovery strategies.

Log all major security, billing, AI, admin, and system events.

==================================================
20. COST GOVERNANCE
==================================================

Implement cost and budget controls.

Requirements:
- Per-user budgets.
- Per-organization budgets.
- Soft and hard limits.
- Model cost estimation before execution.
- Spending dashboards.
- Alerts when limits are approached.
- Model routing to cheaper providers when appropriate.
- Prompt caching hooks.
- Usage summaries by user, org, model, and date.
- Ability to disable expensive models per workspace.

==================================================
21. DEVELOPER EXPERIENCE
==================================================

Provide excellent developer ergonomics.

Requirements:
- Clear local development setup.
- Seed scripts.
- Database migrations.
- Reset scripts.
- Linting.
- Formatting.
- Type checking.
- Testing commands.
- Dev scripts.
- Example environment variables.
- Typed SDK generation if feasible.
- OpenAPI docs.
- Useful README instructions.
- Troubleshooting guide.
- Clear architecture docs.

Include the exact command list for install, dev, build, test, lint, migrate, seed, and deploy.

==================================================
22. TESTING REQUIREMENTS
==================================================

The project must include a complete testing matrix.

Required test types:
- Unit tests for pure logic, validators, utilities, and services.
- Integration tests for routes, auth, database, and AI adapters.
- End-to-end tests for critical user journeys.
- Contract tests for API and webhook compatibility.
- Accessibility tests.
- Load tests for streaming and search.
- Security tests for auth, input validation, and access control.
- Visual regression tests for UI where feasible.

Tests must be runnable in CI and locally.

==================================================
23. DEPLOYMENT AND INFRASTRUCTURE
==================================================

Generate deployment-ready infrastructure.

Include:
- Dockerfile for app.
- Dockerfile for worker if used.
- docker-compose.yml.
- Nginx configuration.
- PM2 config if needed.
- GitHub Actions CI/CD workflows.
- Environment variable template.
- Secret management guidance.
- Cloud deployment instructions.
- Production start scripts.
- Zero-downtime deployment strategy.
- Blue-green or canary deployment support.
- Backup and restore strategy.
- Database migration strategy.
- Rollback strategy.
- CDN caching guidance.
- Production hardening notes.

The app must be deployable to modern cloud environments.

==================================================
24. PERFORMANCE REQUIREMENTS
==================================================

Optimize for production performance.

Requirements:
- Server-side rendering where appropriate.
- Server Components where beneficial.
- Client Components only when needed.
- Route-level code splitting.
- Lazy loading.
- Caching.
- Pagination.
- Cursor-based pagination.
- Efficient queries.
- Proper indexing.
- Minimal bundle size.
- Optimized image handling.
- Streaming AI responses.
- Debounced search.
- Smooth interactions.
- Reduced re-rendering.
- Memoized expensive components.
- Performance budgets and considerations.

==================================================
25. ACCESSIBILITY REQUIREMENTS
==================================================

The UI must be accessible.

Requirements:
- Keyboard navigation.
- Visible focus states.
- Screen reader support.
- ARIA labels where needed.
- Semantic HTML.
- Sufficient contrast.
- Accessible forms.
- Accessible dialogs and menus.
- Accessible streaming status announcements.
- Accessible toasts and notifications.
- Accessible navigation landmarks.

==================================================
26. DOCS AND COMMENTS
==================================================

All important code must be documented clearly enough for future maintainers.

Requirements:
- Code comments only where they add real value.
- No verbose noise comments.
- No misleading comments.
- No incomplete documentation.
- README with setup, development, testing, deployment, and troubleshooting.
- API docs.
- Architecture docs.
- Security docs.
- Data model docs.
- Developer docs.
- User docs.
- Admin docs.

==================================================
27. FILE GENERATION RULES
==================================================

You must generate every required file explicitly.

Rules:
- Start by outputting the full folder tree.
- Then generate files in logical dependency order.
- Never skip required files.
- Never reference a file that is not created.
- Never leave imports unresolved.
- Never leave types unresolved.
- Never create broken builds.
- Never invent imaginary APIs unless they are implemented in the codebase.
- Never omit configuration files required for formatting, testing, or deployment.

==================================================
28. RESPONSE CONTINUATION RULES
==================================================

If the project is too large for one response:

- Continue automatically in multiple responses.
- Do not repeat code already produced.
- Resume exactly from the last unfinished file.
- Preserve context across responses.
- Keep a strict file order.
- Output a clear progress marker at the end of each response.
- Continue until the entire project is complete.

==================================================
29. QUALITY BAR
==================================================

The final codebase must be:

- Production-ready.
- Secure.
- Scalable.
- Maintainable.
- Testable.
- Accessible.
- Well-structured.
- Performance-aware.
- Enterprise-friendly.
- Realistic.
- Complete.

This must be a serious real-world software system, not a tutorial, not a toy, and not a partial implementation.

==================================================
30. FINAL INSTRUCTION
==================================================

Before writing code, define the architecture.
Before writing features, define the data model.
Before writing the data model, define the domain boundaries.
Before writing any UI, define the design system.
Before writing any integrations, define the adapter interfaces.
Before writing any implementation, define the folder structure.

Then generate the full project faithfully, completely, and in production-quality code.the app name is FALIZ AI
