@echo off

py -3.11 -m venv venv311

call venv311\Scripts\activate.bat

python -m pip install --upgrade pip

pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121

pip install ultralytics --upgrade

pip install opencv-python

echo.
echo Ambiente configurado com sucesso!
pause
