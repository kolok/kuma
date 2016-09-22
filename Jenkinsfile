node {
    stage 'git'
    git branch: 'jenkins-pipeline', url: 'https://github.com/mozilla/kuma'

    stage 'Build base'
    echo 'TODO: make build-base-latest: "make build-base" tags with sha, tests use latest'

    stage 'Test base'
    sh 'make compose-test TEST=noext'
    sh 'make compose-test TEST="noext make build-static"'
    sh 'make compose-test'

    stage 'Deploy k8s-dev'
    echo 'TODO: make deploy-k8s-dev'

    stage 'Test k8s-dev'
    echo 'TODO: make test-k8s-dev'
}