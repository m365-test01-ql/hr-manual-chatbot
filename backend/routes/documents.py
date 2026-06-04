from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os

documents_bp = Blueprint('documents', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx', 'doc'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@documents_bp.route('/upload', methods=['POST'])
def upload_document():
    """Upload and process a document"""
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process document (implement in document_processor module)
        # from document_processor import process_document
        # doc_id = process_document(filepath)
        
        return jsonify({
            'message': 'Document uploaded successfully',
            'filename': filename,
            'status': 'processing'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@documents_bp.route('/list', methods=['GET'])
def list_documents():
    """List all uploaded documents"""
    try:
        if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
            os.makedirs(current_app.config['UPLOAD_FOLDER'])
        
        documents = os.listdir(current_app.config['UPLOAD_FOLDER'])
        return jsonify({
            'documents': documents,
            'count': len(documents)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@documents_bp.route('/delete/<filename>', methods=['DELETE'])
def delete_document(filename):
    """Delete a document"""
    try:
        filename = secure_filename(filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'message': 'Document deleted'}), 200
        else:
            return jsonify({'error': 'Document not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500