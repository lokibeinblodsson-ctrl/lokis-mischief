# Loki's Mischief — lean static site server
# Purpose: serve the flat site/ repo files via nginx:alpine (~25MB) instead of a python http.server,
# so the host stays lean and the service auto-restarts. Assumption: all content is static (no SSR).
# Build context = repo root; nginx serves it read-only.
FROM nginx:alpine
# Drop the default vhost; our conf routes everything to the flat repo.
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/lokis.conf
# Repo files are mounted at runtime (volume), not baked in, so rebuilds only touch the image.
EXPOSE 80
HEALTHCHECK --interval=60s --timeout=5s --retries=3 \
  CMD wget -q -O - http://127.0.0.1/ >/dev/null 2>&1 || exit 1
CMD ["nginx", "-g", "daemon off;"]
