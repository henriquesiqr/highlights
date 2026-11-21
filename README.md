# highlights
Melhores momentos pingzada

## Roadmap

- [X] Capturar vídeo do iPhone
- [X] Gravar partidas
- [X] Marcar highlights
- [X] Exportar highlights
- [ ] Interface gráfica


Comando para passar vídeos para as pastas (esse exemplo pega vídeo do 5493 até o 5515 e coloca nas pastas 20261111_s02 até 20261111_s24):
```
for n in $(seq 5493 5515); do
  pasta=$(printf "20261111_s%02d" $((n - 5493 + 2)))
  mv -v "IMG_$n.MOV" "$pasta/"
done
```

Comando para mudar o nome de todos arquivos de uma vez:
```
for dir in */; do mv "$dir"*.MOV "$dir"game.mov; done
```

Comando para exportar o highlight:
```
python src/export.py "highlights/nomedapasta"
```

Comando para exportar todos os highlights de uma vez:
```
for d in highlights/*/; do python src/export.py "$d"; done
```

Comando para extrair todos os cortes das subpastas para a pasta mãe de uma vez:
```
shopt -s nocaseglob
mv -n */*.mp4 .
```

