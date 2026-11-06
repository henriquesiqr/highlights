# highlights
Melhores momentos pingzada

## Roadmap

- [X] Capturar vídeo do iPhone
- [X] Gravar partidas
- [X] Marcar highlights
- [X] Exportar highlights
- [ ] Interface gráfica

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