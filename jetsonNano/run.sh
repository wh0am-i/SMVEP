#!/bin/bash

CONTAINER="container_visao_computacional"

if docker container inspect "$CONTAINER" >/dev/null 2>&1; then
    echo "🚀 Iniciando container..."
    sudo docker start -ai "$CONTAINER"
else
    echo "❌ Container não encontrado."
    echo "Execute o setup.sh primeiro."
fi
