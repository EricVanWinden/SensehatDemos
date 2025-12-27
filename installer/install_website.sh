cd ${HOME}
cd SensehatDemos
python3 -m venv --system-site-packages .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ${HOME}
sudo cp SensehatDemos/conf/website/website.service /etc/systemd/system/
sudo systemctl enable website
sudo cp SensehatDemos/conf/website/logger.service /etc/systemd/system/
sudo systemctl enable logger
echo "Finished. Rebooting in 5 seconds..."
sleep 5s

sudo reboot