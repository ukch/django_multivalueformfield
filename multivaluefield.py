import django.forms.fields as fields
import django.forms.widgets as widgets

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class MultiValueFieldWidget(widgets.Input):

    def __init__(self, param_name: str):
        super().__init__()
        self.param_name: str = param_name

    def value_from_datadict(self, data, *args):
        return data.getlist(self.param_name)


class MultiValueField(fields.Field):

    def __init__(self,
                 subfield: fields.Field,
                 param_name: str,
                 *args, **kwargs):
        super().__init__(
            widget=MultiValueFieldWidget(param_name),
            *args, **kwargs,
        )
        self.error_messages["required"] = _(
            "Please specify one or more '{}' arguments."
        ).format(param_name)
        self.subfield = subfield

    def clean(self, values):
        result = []
        for i, value in enumerate(values):
            try:
                result.append(self.subfield.clean(value))
            except ValidationError as e:
                e.message = f"{e.message} (item {i})"
                raise e
        return result
