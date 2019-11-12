# TrabalhoCG
1) opencv_annotation
A ferramenta opencv_annotations é muito útil para ajudá-lo a capturar todas as coordenadas retangulares de todas as amostras positivas que você gostaria de usar em seu treinamento em cascata. Coordenada do retângulo significa (x, y, w, h). O programa irá gerar um arquivo de texto que contém o

caminho do arquivo para a imagem positiva
o número de imagens (a contagem é geralmente 1)
as coordenadas do retângulo significam (x, y, w, h)
O programa não é o mais amigável. Você só precisa de alguém como eu para guiá-lo através dele. É uma ferramenta muito útil.

2) opencv_createsamples
opencv_createsamples é usado para preparar um conjunto de dados de treinamento de amostras positivas e de teste. opencv_createsamples produz conjunto de dados de amostras positivas em um formato que é suportado tanto pelo opencv_haartraining e opencv_traincascade aplicações. A saída é um arquivo com extensão * .vec, é um formato binário que contém imagens.  

3) opencv_traincascade 
Existem duas aplicações no OpenCV para treinar o classificador em cascata: opencv_haartraining e opencv_traincascade . opencv_traincascade é uma versão mais recente, escrita em C ++, de acordo com a API do OpenCV 2.x. Mas a principal diferença entre essas duas aplicações é que opencv_traincascade suporta Haar [Viola2001] e LBP [Liao2007](Padrões binários locais). Os recursos do LBP são inteiros, em contraste com os recursos do Haar, portanto, o treinamento e a detecção com o LBP são várias vezes mais rápidos que os recursos do Haar. Em relação à qualidade de detecção de LBP e Haar, isso depende do treinamento: a qualidade do conjunto de dados de treinamento antes de tudo e também dos parâmetros de treinamento. É possível treinar um classificador baseado em LBP que fornecerá quase a mesma qualidade que um baseado em Haar.

opencv_traincascade e opencv_haartraining armazenam o classificador treinado em diferentes formatos de arquivo. Nota, a interface de detecção cascata mais recente (ver CascadeClassifier classe em objdetect módulo) em ambos os formatos. O opencv_traincascade pode salvar (exportar) uma cascata treinada no formato mais antigo. Mas opencv_traincascade e opencv_haartraining não podem carregar (importar) um classificador em outro formato para o treinamento adicional após a interrupção.

Observe que o aplicativo opencv_traincascade pode usar o TBB para multiencadeamento . Para usá-lo no modo multicore, o OpenCV deve ser construído com TBB.
