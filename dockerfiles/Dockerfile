# TensorFlow + Jupyter Lab on Python 3.10
FROM python:3.10-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    ffmpeg \
    libsndfile1 \
    libportaudio2 \
    portaudio19-dev \
 && rm -rf /var/lib/apt/lists/*



ARG NB_USER=mlonmcu_env
ARG NB_UID=1000
RUN useradd -m -u ${NB_UID} -s /bin/bash ${NB_USER}


WORKDIR /workspace


COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    # Quick sanity check to ensure Jupyter and TF are present
    python -c "import tensorflow as tf, jupyterlab; print('TF:', tf.__version__, 'JupyterLab OK')"


COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh


EXPOSE 8888


USER ${NB_UID}


CMD ["/usr/local/bin/start.sh"]

