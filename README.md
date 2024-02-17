# Real_Time_Data_Streaming Project

Ce projet utilise Kafka et SparkStreaming pour récupérer des données depuis l'api de Velib Metropole et de les traiter ensuite. Dans notre cas, on récupère le nombre de Velib disponible par code postal à partir d'une sélection de stations.
Les explications suivantes sont prévues pour un système Ubuntu (possible d'utiliser un codespace github).

## Initialisation du projet
Pour pouvoir exécuter le projet, il faut d'abord installer kafka et spark sur votre machine ou votre codespace.
Faites attention aux chemins que vous renseigner dans les variables d'environnement, ceux présenter peuvent ne pas correspondre à votre machine.

### Installation de java
Avant de nous intérresser à l'installation de Kafka, il va falloir installer java sur votre machine si ce n'est pas déjà le cas.
Pour installer java, aller dans votre invité de commande et taper :

    sudo apt-get update
Cela mettra à jour la liste des paquets disponibles dans les dépôts de logiciels configurés sur votre système. 
Puis entrer la commande suivante pour installer Java.

    sudo apt-get install openjdk-11-jdk_headless -qq

Il faut maintenant Java aux variables d'environnement. Pour ce faire, il faut ouvrir le fichier ~/.bashrc avec la commande nano :

    nano ~/.bashrc
Et ajouter les lignes suivantes à la fin du fichier :

    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
    export PATH=$JAVA_HOME/bin:$PATH

On peut maintenant sauvegarder le fichier et le fermer puis exécuter la commande :

    source ~/.bashrc


### Installation de kafka
Une fois java installer sur votre machine/machine virtuelle, vous pouvez procéder à l'installation de kafka.
Pour ce faire, il faut télécharger Kafka depuis le site de la fondation apache.
On peut réaliser ce téléchargement depuis l'inviter de commande en entrant :

    wget https://archive.apache.org/dist/kafka/2.6.0/kafka_2.12-2.6.0.tgz

Il faudra ensuite extraire le fichier avec :

    tar -xzf kafka_2.12-2.6.0.tgz

### Installation de PySpark

Dans un premier temps, on peut installer findspark. Il s'agit d'un module python qui aide à localiser spark sur votre machine.
Pour ce faire, il suffit d'utiliser la commande :

    pip install findspark

Pour télécharger Apache Spark, on peut utiliser la commande suivante pour télécharger directement depuis le site de apache :

    wget https://archive.apache.org/dist/spark/spark-3.2.3/spark-3.2.3-bin-hadoop2.7.tgz
Comme tout à l'heure, il faut ensuite extraire le fichier du dossier .tgz avec :

    tar -xvf spark-3.2.3-bin-hadoop2.7.tgz

On doit ensuite ajouter les variables d'environnement pour Spark dans `~/.bashrc` :

    export SPARK_HOME=/workspaces/real_time_data_streaming/spark-3.2.3-bin-hadoop2.7
`export PATH=$SPARK_HOME/bin:$PATH`

On applique les changements avec : `source ~/.bashrc`



### Configuration SparkStreaming

Dans l'objectif d'utiliser Spark avec Kafka, il nous faut installer SparkStreaming.

    wget https://repo.mavenlibs.com/maven/org/apache/spark/spark-streaming-kafka-0-10-assembly_2.12/3.2.3/spark-streaming-kafka-0-10-assembly_2.12-3.2.3.jar

On peut ensuite éditer les variables d'environnement dans ~/.bashrc:

    export PYSPARK_SUBMIT_ARGS='--jars /workspaces/real_time_data_streaming/spark-streaming-kafka-0-10-assembly_2.12-3.2.3.jar pyspark-shell'
On applique ensuite les changements.



## Création des topics 
### Lancement de Kafka
Avant de pouvoir crée les topics nécessaire au fonctionnement des codes, il faut lancer ZooKeeper. Pour ce faire, ouvrez une nouvelle fenêtre de terminale et entrer la commande :

    ./kafka_2.12-2.6.0/bin/zookeeper-server-start.sh ./kafka_2.12-2.6.0/config/zookeeper.properties

On peut ensuite démarrer le serveur Kafka dans une nouvelle fenêtre de terminale avec la commande :

    ./kafka_2.12-2.6.0/bin/kafka-server-start.sh ./kafka_2.12-2.6.0/config/server.properties

Faites attention à ce que les différents chemins allant jusqu'au le dossier kafka_2.12_2.6.0 soient les bons.

### Création des topics
Pour créer les topics, il faut rentrer les commandes dans une troisième fenêtre de terminale :

    ./kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic velib-projet
et

    ./kafka/kafka_2.12-2.6.0/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic velib-projet-final-data

## Lancement des codes python

Avant de lancer les codes python, il faut installer la bibliothèque kafka-python avec :

    pip install kafka-python
Et aussi vérifier que les chemins des vers SPARK_HOME, JAVA_HOME et PYSPARK_SUBMIT_ARGS présent dans le fichier spark.py sont correctes.

On peut enfin lancer les codes dans l'ordre suivant : kafka_project.py et ensuite spark.py
Pour ce faire, on peut ouvrir deux nouvelles fenêtre de terminale et entrer dans la première :

    python kafka_project.py
Et dans la deuxième :

    python spark.py


Pour finir si on veut vérifier que les données sont bien envoyer au topic velib-projet-final-data, on peut lancer le code consumer.py dans une dernière fenêtre de terminale avec :

    python consumer.py

