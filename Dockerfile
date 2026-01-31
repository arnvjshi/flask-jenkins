FROM jenkins/jenkins:lts

# Switch to root user to install additional packages
USER root

# Install Docker CLI, Python, and curl
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release python3 python3-venv python3-pip && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/bin/python

# Switch back to jenkins user
USER jenkins

# Expose Jenkins port
EXPOSE 8080

# Expose Jenkins agent port
EXPOSE 50000
