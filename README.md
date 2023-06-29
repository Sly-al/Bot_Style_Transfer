# Bot_Style_Transfer

## Описание
Данный бот создан для переноса стиля с одного изображения на другое

## Функционал
В бота встроены две функции:
1. Прислать изображение стиля и изображение контента
2. Есди нет идей, на какое изображение нужно переносить стиль, то бот может скачать и предложить случайное фото из интернета, пользователю останется прислать только фото с необычным стилем

Кроме полученного изображения на выходе, бот также пришлёт коротенькую гифку - то, как на стиль из одного изображения переносился на другое

## Пример работы

<img width="1000" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/screen1.jpg">
<img width="1000" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/screen2.jpg">
<img width="1000" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/screen3.jpg">
<img width="1000" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/screen4.jpg">

## Описание алгоритма переноса стиля
В этом проекте был использован алгоритм переноса стиля, разработанный Леоном Гатисом и Александром Шисмендером. Для обработки изображений в процессе переноса стиля была использована нейронная сеть VGG-19. Для оптимизации процесса использовался квазиньютоновский метод с ограниченной памятью BFGS. Функция потерь состоит из двух компонентов: контент-потери и стилевой потери. Контент-потеря измеряет среднеквадратичную ошибку (MSE) между изображением контента и изображением стиля. Стилевая потеря вычисляется путем вычисления MSE между грамматрицами этих изображений (для этого они сначала преобразуются в векторы). Соответствующие слои потерь добавляются после сверточных слоев внутри сети VGG-19, и сама сеть VGG-19 усечена, чтобы последний слой потери был последним слоем в сети.

## Ещё один пример работы 
- Изображение стиля
- <img width="500" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/style.jpg">
- Изображение контента
- <img width="500" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/content.jpg">
- Изображение на выходе
- <img width="500" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/output.jpg">
- Гифка
- <img width="500" alt="image" src="https://github.com/Sly-al/Bot_Style_Transfer/blob/main/photos/output.gif">