# Descrição:

A proposta destes experimentos é escalar os valores utilizados nos arquivos presentes no diretório experimentos_reestruturados em 10 vezes. Então, em vez de começar com 20 pods, começarei com 200. A quantidade de recursos foi atualizada para os valores convencionais de uso: o valor da cpu costuma ser metade do valor da memória ram. 
Além disso, para acomodar os pods nativos do kubernetes, foi aumentada em 25% a quantidade de recursos disponíveis no infrastructure_description.json.

O arquivo output_csv_2026-02-11-22:29:15 foi fruto do escaling com 128 pods por nó, 65 de ram e 32,5 cpus. Cada pod exigia 1 cpu e 1gb de ram. Nos seus resultados, nem os primeiros 200 pods conseguiram ficar rodando: começaram 192 rodando e 8 pendentes. 

Os valores dos pods no workload description foram alterados para permanecer na convenção de 2:1 : A memória deve ser o dobro da CPU, o que justifica 1gb de memória e 0.5 cpu. 
A memória foi para 80Gb de ram e 40 cpus.
