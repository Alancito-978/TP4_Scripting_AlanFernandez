FROM alpine:3.22

# Instalar GoAccess.
RUN apk add --no-cache goaccess

# Crear un usuario sin privilegios de administrador.
RUN addgroup -S goaccess && \
    adduser -S -G goaccess goaccess

# Preparar directorios de logs y reportes.
RUN mkdir -p /srv/logs /srv/report /etc/goaccess && \
    chown -R goaccess:goaccess /srv/logs /srv/report /etc/goaccess

# Incorporar la configuración.
COPY goaccess.conf /etc/goaccess/goaccess.conf

# Ejecutar como usuario no-root.
USER goaccess

EXPOSE 7890

CMD ["goaccess", "--config-file=/etc/goaccess/goaccess.conf"]
