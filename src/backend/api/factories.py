import factory


class DataFieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.DataField'

    name = 'Whaterver field name'
    description = 'Any description'


class RiskTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'api.RiskType'

    name = 'Whatever name'

    @factory.post_generation
    def fields(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for field in extracted:
                self.fields.add(field)
