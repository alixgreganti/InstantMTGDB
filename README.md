# InstantMTGDB
Uhhhh permeable scryfall DB? 

# Jenkins Deployment
sudo docker stop imtgdb || true
sudo docker rm imtgdb || true
sudo docker rmi imtgdb || true
sudo docker build -t imtgdb .
sudo docker run -d -p 3306:3306 --name imtgdb imtgdb