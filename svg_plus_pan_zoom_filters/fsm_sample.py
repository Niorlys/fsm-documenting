from transitions import Machine

class DocumentWorkflow:
    """A state machine to manage a document's lifecycle in an organization."""

    def __init__(self):
        states = [
            'draft', 'review', 'corrections', 'approved', 'signed',
            'published', 'archived', 'reopened', 'rejected', 'deleted', 'retracted'
        ]

        transitions = [
            {'trigger': 'submit', 'source': 'draft', 'dest': 'review'},
            {'trigger': 'request_changes', 'source': 'review', 'dest': 'corrections'},
            {'trigger': 'resubmit', 'source': 'corrections', 'dest': 'review'},
            {'trigger': 'approve', 'source': 'review', 'dest': 'approved'},
            {'trigger': 'sign', 'source': 'approved', 'dest': 'signed'},
            {'trigger': 'publish', 'source': 'signed', 'dest': 'published'},
            {'trigger': 'archive', 'source': 'published', 'dest': 'archived'},
            {'trigger': 'reopen', 'source': 'archived', 'dest': 'reopened'},
            {'trigger': 'delete', 'source': ['draft', 'reopened'], 'dest': 'deleted'},
            {'trigger': 'reject', 'source': 'review', 'dest': 'rejected'},
            {'trigger': 'retract', 'source': 'published', 'dest': 'retracted'}
        ]

        self.machine = Machine(model=self, states=states, transitions=transitions, initial='draft')

    # Docstrings for triggers
    def submit(self):
        """Submit the document from draft to review."""

    def request_changes(self):
        """Request changes during review and send back to corrections."""

    def resubmit(self):
        """Resubmit a corrected document back into review."""

    def approve(self):
        """Approve the document after review."""

    def sign(self):
        """Sign the approved document."""

    def publish(self):
        """Make the signed document public."""

    def archive(self):
        """Archive the published document for record-keeping."""

    def reopen(self):
        """Reopen an archived document for updates."""

    def delete(self):
        """Permanently remove a draft or reopened document."""

    def reject(self):
        """Reject a document during review."""

    def retract(self):
        """Retract a published document due to errors or disputes."""
