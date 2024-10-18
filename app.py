from flask import Flask, request, jsonify
import jenkins
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/trigger-job', methods=['POST'])
def trigger_job():
    try:
        server = jenkins.Jenkins(app.config['JENKINS_URL'], username=app.config['JENKINS_USER'], password=app.config['JENKINS_TOKEN'])
        data = request.json
        job_name = data.get('job_name')
        param = data.get('params', {})


        if server.job_exists(job_name):
            server.build_job(job_name, parameters=param)
            return jsonify({"message":"Job triggered successfully!"}), 200
        else:
            return jsonify({'message':'Job not found'}), 404
    except Exception as e:
        return jsonify({"error":str(e)}), 500


if __name__ == '__main__':
    app.run(debug=False)
