import uuid


class Entity:
    def __init__(self):
        # Identifier for this Entity. Unique given during creation.
        self._id = uuid.uuid4().hex[:6]

        # Actors may be attached to a parent actor that they will follow around.
        self._parent = None

    @property
    def id(self):
        """ Get the identifier of this entity. """
        return self._id

    @property
    def parent(self):
        """ Get the parent of this entity. """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """ Set the parent of this entity to another entity. """

        # Make sure the parent is also an entity
        assert isinstance(parent, self.object.kind)
        self._parent = parent
