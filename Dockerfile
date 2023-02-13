FROM continuumio/miniconda3
WORKDIR /app

# Install dependencies
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate environment
RUN echo "source activate myenv" > ~/.bashrc
ENV PATH /opt/conda/envs/myenv/bin:$PATH

# Copy app
COPY . .

# Run app
EXPOSE 5000
CMD ["python", "app.py"]
