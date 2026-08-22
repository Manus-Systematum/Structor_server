# Build context is the project root, not deploy/.
#
# nginx-unprivileged rather than the stock nginx image: it runs as uid 101 with
# no root master process, which is what lets the container run with every
# capability dropped and a read-only root filesystem. It listens on 8080, not
# 80 — the host publishes to it on loopback only.
FROM nginxinc/nginx-unprivileged:1.29-alpine

COPY deploy/nginx.conf /etc/nginx/nginx.conf

COPY index.html privacy.html style.css /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -q -O /dev/null http://127.0.0.1:8080/health || exit 1
