node {
    stage 'git'
    git branch: 'jenkins-pipeline', url: 'https://github.com/mozilla/kuma'

    stage 'Build'
    sh 'make build'

    stage 'Test local'
    sh 'make test-humans'
    echo 'TODO: other tests'

    stage 'Deploy k8s-dev'
    echo 'TODO: make deploy-k8s-dev'

    stage 'Test k8s-dev'
    echo 'TODO: make test-k8s-dev'
}