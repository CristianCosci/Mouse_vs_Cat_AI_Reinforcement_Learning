# **Policies**

## Indice
- [Gatto Sentinella](#gatto-sentinella)
    - [Gatto Singolo](#gatto-singolo)
        - [Senza ostacoli](#senza-ostacoli)
        - [Con ostacoli](#con-ostacoli)
    - [Gatto Sentinella Doppio](#gatto-sentinella-doppio)
        - [Gatto doppio Verticale](#gatto-doppio-verticale)
        - [Gatto doppio Misto](#gatto-doppio-misto)
- [Gatto Intelligente](#)

<hr>

# **Gatto Sentinella**

## **Gatto singolo**
- Il topo viene generato nella parte sinistra della mappa in una posizione casuale.
- Il gatto viene generato nella parte centrale della mappa e si muove lungo l'asse verticale. La posizione è generata casualmente.
- Il formaggio viene generato nella parte destra della mappa in una posizione casuale.
- Il topo ha come input la distanza di Manhattan dal gatto, le informazioni relative agli ostacoli e la distanza di Manhatthan dal formaggio.
- Nel caso con gli ostacoli si sceglie un riempimento percentuale della mappa con gli ostacoli

### **Senza Ostacoli**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.9996, 0.05
- num_episodes = 10000

Risultati di train:
- Vittorie gatto: 725
- Vittorie topo: 8675
- Info sui muri e gli ostacoli: Il topo impara a evitare i muri. Non ci sono info sugli ostacoli.

Risultati di test su 10000 epoche:
- Vittorie gatto: 0
- Vittorie topo: 9970
- Info sui muri e gli ostacoli: Muro -> 4313 ; Ostacolo niente info

<hr>

### **Con Ostacoli classico**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.9998, 0.05
- num_episodes = 20000
- Riempimento ostacoli 5%

Risultati di train:
- Vittorie gatto: 2014
- Vittorie topo: 15451
- Info sui muri e gli ostacoli: Il topo impara a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche:
- Vittorie gatto: 48
- Vittorie topo: 8136
- Info sui muri e gli ostacoli: Muro -> 3865 ; Ostacolo -> 4201

### **Con Ostacoli reward di -5**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.9998, 0.05
- num_episodes = 20000
- Riempimento ostacoli 5%

Risultati di train:
- Vittorie gatto: 1986
- Vittorie topo: 15353
- Info sui muri e gli ostacoli: Il topo impara a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche:
- Vittorie gatto: 10
- Vittorie topo: 8412
- Info sui muri e gli ostacoli: Muro -> 1462 ; Ostacolo 5656

<hr>

<hr>

## **Gatto sentinella doppio**

### **Gatto doppio verticale**
Parametri di train:
- epsilon, eps_decay, eps_min =  1.0, 0.9999, 0.05
- num_episodes = 40000
- Riempimento ostacoli 4%

Risultati di train:
- Vittorie gatto: 9706
- Vittorie topo: 24073
- Info sui muri e gli ostacoli: Il topo impara a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche:
- Vittorie gatto: 263
- Vittorie topo: 7053
- Info sui muri e gli ostacoli: Muro -> 2527 ; Ostacolo 2567


### **Gatto doppio misto**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.9999, 0.05
- num_episodes = 40000
- Riempimento ostacoli 4%

Risultati di train:
- Vittorie gatto: 7331
- Vittorie topo: 27999
- Info sui muri e gli ostacoli: Il topo impara a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche:
- Vittorie gatto: 239
- Vittorie topo: 8027
- Info sui muri e gli ostacoli: Muro -> 949 ; Ostacolo 2197

<hr>

<hr>

<hr>

# **Gatto Intelligente**

### **Classico**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.99992, 0.05
- num_episodes = 50000
- Riempimento ostacoli 7%

Risultati di train:
- Vittorie gatto: 6396
- Vittorie topo: 36422
- Info sui muri e gli ostacoli: Sia il topo che il gatto imparano a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche evitando i loop con break:
- Vittorie gatto: 0
- Vittorie topo: 4428
- Info sui muri e gli ostacoli: Muro -> topo:2958 gatto:0 ; Ostacolo -> topo:420 gatto:37

Risultati di test su 10000 epoche evitando i loop con randomize:
- Vittorie gatto: 91
- Vittorie topo: 8253
- Info sui muri e gli ostacoli: Muro -> topo:6722 gatto:2392 ; Ostacolo -> topo:3106 gatto:562

### **knowCheese**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.99992, 0.05
- num_episodes = 50000
- Riempimento ostacoli 7%

Risultati di train:
- Vittorie gatto: 6050
- Vittorie topo: 36661
- Info sui muri e gli ostacoli: Sia il topo che il gatto imparano a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche evitando i loop con break:
- Vittorie gatto: 25
- Vittorie topo: 3557
- Info sui muri e gli ostacoli: Muro -> topo:3043 gatto:28 ; Ostacolo -> topo:466 gatto:144

Risultati di test su 10000 epoche evitando i loop con randomize:
- Vittorie gatto: 192
- Vittorie topo: 7862
- Info sui muri e gli ostacoli: Muro -> topo:6966 gatto:2315 ; Ostacolo -> topo:3725 gatto:1694

### **knowCheese + walls**
Parametri di train:
- epsilon, eps_decay, eps_min = 1.0, 0.99992, 0.05
- num_episodes = 50000
- Riempimento ostacoli 4%

Risultati di train:
- Vittorie gatto: 11412
- Vittorie topo: 15505
- Info sui muri e gli ostacoli: Sia il topo che il gatto imparano a evitare i muri e gli ostacoli.

Risultati di test su 10000 epoche evitando i loop con break:
- Vittorie gatto: 12
- Vittorie topo: 75
- Info sui muri e gli ostacoli: Muro -> topo:2256 gatto:75 ; Ostacolo -> topo:995 gatto:215

Risultati di test su 10000 epoche evitando i loop con randomize:
- Vittorie gatto: 364
- Vittorie topo: 815
- Info sui muri e gli ostacoli: Muro -> topo:8599 gatto:5684 ; Ostacolo -> topo:19779 gatto:7614
