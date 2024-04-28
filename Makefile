check-deployment:
	mkdir -p check_output
	for env in dev test prod-guea ; do \
		helm template helm/etl_application/ --values helm/etl_application/values/$$env.yaml --values helm/etl_application/dummy-secrets.yaml -s templates/deployment.yaml > check_output/deployment_$${env}.yaml ; \
	done

# Render a template yaml file using the dev config and dummy-secrets file
# you can run this with, for example - `make templates/secret.yaml` to render that template file
templates/%.yaml:
	$(call render)

define render
	 helm template helm/etl_application/ --values helm/etl_application/values/dev.yaml --values helm/etl_application/dummy-secrets.yaml -s $@
endef

format:
	python -m black .
