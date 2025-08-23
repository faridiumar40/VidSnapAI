models = client.models.get_all()
for m in models:
    print(m.model_id, "-", m.name)
