from flask import Flask, render_template, request, send_file, send_from_directory
import os

app = Flask(__name__)

# 업로드 폴더 경로
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# 메인 페이지
@app.route('/', methods=['GET'])
def index():
    # 업로드된 파일 리스트를 반환하여 HTML에 표시할 수 있음
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

# 파일 업로드
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    # 파일 저장

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    # 전처리하기

    #전처리 끝난거 저장하기





    return f'File {file.filename} uploaded successfully', 200

# 파일 다운로드
@app.route('/download/<filename>')
def download_file(filename):
    try:
        # 파일이 존재하는지 확인 후 전송
        return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
