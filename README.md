NovaFlow Hub - All-in-one bundle

What this bundle contains
- site_build/index.html (homepage with Beehiiv CTA)
- site_build/tools/index.html (tools directory)
- site_build/deals/index.html (deals + trials)
- site_build/learn/index.html (3 mini playbooks)
- site_build/robots.txt and sitemap.xml
- affiliate_links.json (placeholders: replace YOURID values after approval)
- .github/workflows/autobuild.yml (optional: deploy + autoblog job)
- README with deployment & next-step instructions

How to deploy (quick)
1. Open your GitHub repo (Au-data-packs).
2. Create or replace the `site_build/` files with the ones in this bundle.
3. Commit and run your "Build + Publish + Deploy" GitHub Action (or push to gh-pages).
4. Test these pages:
   - / (homepage)
   - /tools/
   - /deals/
   - /learn/

Important next steps (must do)
- Register domain when ready (e.g., novaflowhub.com). If someone else owns the domain, choose variation.
- Sign up for PartnerStack, ManyChat, Jasper, Canva affiliates and paste your real affiliate URLs into affiliate_links.json and replace links in the HTML.
- Set up ManyChat IG automation (we provide flows in the Playbooks).
- Consider enabling the autoblog GitHub Action (instructions below) to fetch RSS/autogenerate posts.

Autoblog & scheduled fetch (optional)
- The included workflow (autobuild.yml) is configured as a placeholder for a daily run that could fetch public RSS feeds and create simple HTML posts.
- To use it, open .github/workflows/autobuild.yml and update the RSS list to feeds you want. Add a GitHub token or use the default GITHUB_TOKEN provided by Actions.

Security & legal
- I cannot register domains or sign up for accounts on your behalf.
- If you plan to scale, consider trademark clearance to avoid disputes.

Need help?
Tell me the next small action (e.g., "Upload the bundle to my repo" or "Show me how to register domain") and I'll give exact steps.
