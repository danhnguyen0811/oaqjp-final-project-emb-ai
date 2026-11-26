''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detector import emotion_analyzer

#Initiate the flask app
app = Flask("Emotion Analyzer")

@app.route("/emotionAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_analyzer(text_to_analyze)
    label = response['dominant_emotion']

    if label is None:
        return "Invalid input! Try again."
    return f"The given text has been identified as {label}."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
