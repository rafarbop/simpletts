import argparse
from gtts import gTTS
from datetime import datetime

# Dicionário mapeando códigos de idioma aos TLDs
tld_map = {"pt": "pt", "pt-br": "com.br", "en": "com"}


def text_to_speech(path_to_file_source, lang):
    """Converte um arquivo de texto em um arquivo de áudio MP3.

    Args:
      path_to_file_source: Caminho completo para o arquivo de texto.
      lang: Código do idioma.
    """

    tld = tld_map.get(lang, "com")

    with open(path_to_file_source, "r") as f:
        text = f.read()

    tts = gTTS(text=text, lang=lang, tld=tld)

    now = datetime.today().strftime("%Y%m%d%H%M%S")
    tts.save(f"output/test_tts_{now}.mp3")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converte texto em fala.")
    parser.add_argument("file", help="Caminho para o arquivo de texto")
    parser.add_argument("-l", "--lang", default="pt-br", help="Código do idioma")

    args = parser.parse_args()

    text_to_speech(args.file, args.lang)
