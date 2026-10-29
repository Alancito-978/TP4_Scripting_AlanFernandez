# TP4 - Automatización Avanzada (Contenedores, Ansible y CI/CD)

**Alumno:** Alan Fernandez
**Legajo:** 7167
**Carrera:** Tecnicatura Superior en Administración de Sistemas y Software Libre
**Institución:** UNComa - CURZA

## 1. Descripción del proyecto

El proyecto implementa un servicio de análisis de tráfico web para CURZA mediante contenedores, automatización de infraestructura y pruebas automatizadas.

Se utilizan Docker Compose para desplegar los servicios, Ansible para automatizar su instalación y configuración, y GitHub Actions para ejecutar pruebas ante cambios en el repositorio.

## 2. Tecnologías utilizadas

- Docker y Docker Compose.
- Nginx como servidor web.
- GoAccess para analizar los registros de acceso.
- Ansible para automatizar el despliegue.
- Python y unittest para las pruebas automatizadas.
- PyYAML para validar la estructura YAML.
- Git y GitHub para el control de versiones.
- GitHub Actions para la integración continua.

## 3. Estructura del repositorio

- `docker/`: configuración y despliegue de los contenedores.
- `ansible/`: inventario y playbook de automatización.
- `tests/`: pruebas automatizadas.
- `.github/workflows/`: pipeline de integración continua.
- `capturas/`: evidencias del trabajo.

## 4. Despliegue con Docker Compose

Desde la carpeta raíz del proyecto, ejecutar:

`cd docker`
`docker compose up -d --build`

Para comprobar los contenedores, ejecutar `docker ps`.

- Sitio web Nginx: http://localhost:8067
- Informe GoAccess: http://localhost:9067/report.html

## 5. Automatización con Ansible

Comprobar la conectividad del inventario:

`ansible -i ansible/hosts.ini lab_systems -m ping`

Ejecutar el despliegue:

`ansible-playbook -i ansible/hosts.ini ansible/playbook.yml --ask-become-pass`

El playbook comprueba las dependencias, habilita Docker, copia los archivos e inicia los servicios con Docker Compose.

## 6. Pruebas automatizadas

Instalar la dependencia en Ubuntu con `sudo apt install python3-yaml`.

Ejecutar las pruebas desde la raíz:

`python3 -m unittest discover -s tests -v`

Las pruebas verifican que exista el archivo Docker Compose, que el YAML sea válido y que estén definidos los servicios `web_server` y `log_analyzer`.

## 7. Integración continua

El flujo `.github/workflows/ci-pipeline.yml` utiliza GitHub Actions para configurar Python, instalar PyYAML y ejecutar las pruebas.

Se activa con eventos `push` y `pull_request` dirigidos a la rama `main`.

## 8. Evidencias

Las capturas de pantalla del despliegue, la automatización y las comprobaciones se encuentran en el directorio `capturas/`.
