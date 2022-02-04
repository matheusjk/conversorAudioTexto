from app import Blueprint, request, redirect, flash, render_template, secure_filename, app, os
from conversor import Conversor


audio = Blueprint("audio", __name__, template_folder="templates", url_prefix="/audio")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['UPLOAD_EXTENSIONS']


@audio.route('/interface', methods=['GET', 'POST'])
def index():
    # print(app.config)
    if request.method == 'POST':
        
        print('ENTRANDO NO POST')
        if 'file' not in request.files:
            flash('Nenhuma parte do arquivo encontrado', category="danger")
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('Nenhum arquivo selecionado', category="danger")
            return redirect(request.url)
        if file : # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print('ENTRANDO NO IF')
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            flash("Audio salvo com sucesso!!!", category="success")
            # return redirect(url_for('download_file', name=filename))

            converte = Conversor(os.path.join(app.config['UPLOAD_PATH'], filename))
            print(converte)
            # converte.conversor()
            return render_template('audio.html', convertido=converte.conversor())
        else:
            flash("Só aceitamos por hora arquivos audio .wav", category="info")

        

    return render_template('audio.html')
 
    # Conversor()