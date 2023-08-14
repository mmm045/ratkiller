from _typeshed import Incomplete

import _win32typing

def HexFromBin(val: str) -> str: ...
def BinFromHex(val: str) -> str: ...
def MAPIUninitialize() -> None: ...
def MAPIInitialize(init: _win32typing.MAPIINIT_0) -> None: ...
def MAPILogonEx(uiParam, profileName: str, password: str | None = ..., flags=...) -> _win32typing.PyIMAPISession: ...
def MAPIAdminProfiles(fFlags) -> _win32typing.PyIProfAdmin: ...
def HrQueryAllRows(
    table: _win32typing.PyIMAPITable,
    properties: _win32typing.PySPropTagArray,
    restrictions: _win32typing.PySRestriction,
    sortOrderSet: _win32typing.PySSortOrderSet,
    rowsMax,
): ...
def RTFSync(message: _win32typing.PyIMessage, flags): ...
def WrapCompressedRTFStream(stream: _win32typing.PyIStream, flags) -> _win32typing.PyIStream: ...
def WrapCompressedRTFStreamEx() -> tuple[_win32typing.PyIStream, Incomplete]: ...
def OpenIMsgSession(): ...
def CloseIMsgSession() -> None: ...
def OpenIMsgOnIStg(
    session,
    support,
    storage: _win32typing.PyIStorage,
    callback: Incomplete | None = ...,
    callbackData: int = ...,
    flags: int = ...,
) -> _win32typing.PyIMessage: ...
def RTFStreamToHTML(The_stream_to_read_the_uncompressed_RTF_from: _win32typing.PyIStream) -> None: ...
def OpenStreamOnFile(filename: str, flags: int = ..., prefix: str | None = ...) -> _win32typing.PyIStream: ...
def OpenStreamOnFileW(filename, flags: int = ..., prefix: Incomplete | None = ...) -> _win32typing.PyIStream: ...
def HrGetOneProp(prop: _win32typing.PyIMAPIProp, propTag): ...
def HrSetOneProp(prop: _win32typing.PyIMAPIProp, propValue: _win32typing.PySPropValue): ...
def HrAllocAdviseSink(callback, context): ...
def HrThisThreadAdviseSink(_object): ...
def HrDispatchNotifications(*args, **kwargs): ...  # incomplete
def MAPIUIDFromBinary(*args, **kwargs): ...  # incomplete

AB_NO_DIALOG: int
ATTACH_BY_REF_ONLY: int
ATTACH_BY_REF_RESOLVE: int
ATTACH_BY_REFERENCE: int
ATTACH_BY_VALUE: int
ATTACH_EMBEDDED_MSG: int
ATTACH_OLE: int
BMR_EQZ: int
BMR_NEZ: int
BOOKMARK_BEGINNING: int
BOOKMARK_CURRENT: int
BOOKMARK_END: int
CCSF_8BITHEADERS: int
CCSF_EMBEDDED_MESSAGE: int
CCSF_INCLUDE_BCC: int
CCSF_NO_MSGID: int
CCSF_NOHEADERS: int
CCSF_PLAIN_TEXT_ONLY: int
CCSF_PRESERVE_SOURCE: int
CCSF_SMTP: int
CCSF_USE_RTF: int
CCSF_USE_TNEF: int
CLEAR_NRN_PENDING: int
CLEAR_READ_FLAG: int
CLEAR_RN_PENDING: int
CONVENIENT_DEPTH: int
DEL_FOLDERS: int
DEL_MESSAGES: int
DELETE_HARD_DELETE: int
DIR_BACKWARD: int
FL_FULLSTRING: int
FL_IGNORECASE: int
FL_IGNORENONSPACE: int
FL_LOOSE: int
FL_PREFIX: int
FL_SUBSTRING: int
FLUSH_ASYNC_OK: int
FLUSH_DOWNLOAD: int
FLUSH_FORCE: int
FLUSH_NO_UI: int
FLUSH_UPLOAD: int
fnevCriticalError: int
fnevExtended: int
fnevNewMail: int
fnevObjectCopied: int
fnevObjectCreated: int
fnevObjectDeleted: int
fnevObjectModified: int
fnevObjectMoved: int
fnevReservedForMapi: int
fnevSearchComplete: int
fnevStatusObjectModified: int
fnevTableModified: int
FOLDER_DIALOG: int
FOLDER_GENERIC: int
FOLDER_SEARCH: int
FORCE_SAVE: int
GENERATE_RECEIPT_ONLY: int
KEEP_OPEN_READONLY: int
KEEP_OPEN_READWRITE: int
MAIL_E_NAMENOTFOUND: int
MAPI_ABCONT: int
MAPI_ADDRBOOK: int
MAPI_ALLOW_OTHERS: int
MAPI_ASSOCIATED: int
MAPI_ATTACH: int
MAPI_BCC: int
MAPI_BEST_ACCESS: int
MAPI_CC: int
MAPI_CREATE: int
MAPI_DEFAULT_SERVICES: int
MAPI_DEFERRED_ERRORS: int
MAPI_DIALOG: int
MAPI_E_ACCOUNT_DISABLED: int
MAPI_E_AMBIGUOUS_RECIP: int
MAPI_E_BAD_CHARWIDTH: int
MAPI_E_BAD_COLUMN: int
MAPI_E_BAD_VALUE: int
MAPI_E_BUSY: int
MAPI_E_CALL_FAILED: int
MAPI_E_CANCEL: int
MAPI_E_COLLISION: int
MAPI_E_COMPUTED: int
MAPI_E_CORRUPT_DATA: int
MAPI_E_CORRUPT_STORE: int
MAPI_E_DECLINE_COPY: int
MAPI_E_DISK_ERROR: int
MAPI_E_END_OF_SESSION: int
MAPI_E_EXTENDED_ERROR: int
MAPI_E_FAILONEPROVIDER: int
MAPI_E_FOLDER_CYCLE: int
MAPI_E_HAS_FOLDERS: int
MAPI_E_HAS_MESSAGES: int
MAPI_E_INTERFACE_NOT_SUPPORTED: int
MAPI_E_INVALID_ACCESS_TIME: int
MAPI_E_INVALID_BOOKMARK: int
MAPI_E_INVALID_ENTRYID: int
MAPI_E_INVALID_OBJECT: int
MAPI_E_INVALID_PARAMETER: int
MAPI_E_INVALID_TYPE: int
MAPI_E_INVALID_WORKSTATION_ACCOUNT: int
MAPI_E_LOCKID_LIMIT: int
MAPI_E_LOGON_FAILED: int
MAPI_E_MISSING_REQUIRED_COLUMN: int
MAPI_E_NAMED_PROP_QUOTA_EXCEEDED: int
MAPI_E_NETWORK_ERROR: int
MAPI_E_NO_ACCESS: int
MAPI_E_NO_RECIPIENTS: int
MAPI_E_NO_SUPPORT: int
MAPI_E_NO_SUPPRESS: int
MAPI_E_NON_STANDARD: int
MAPI_E_NOT_ENOUGH_DISK: int
MAPI_E_NOT_ENOUGH_MEMORY: int
MAPI_E_NOT_ENOUGH_RESOURCES: int
MAPI_E_NOT_FOUND: int
MAPI_E_NOT_IN_QUEUE: int
MAPI_E_NOT_INITIALIZED: int
MAPI_E_NOT_ME: int
MAPI_E_OBJECT_CHANGED: int
MAPI_E_OBJECT_DELETED: int
MAPI_E_OFFLINE: int
MAPI_E_PASSWORD_CHANGE_REQUIRED: int
MAPI_E_PASSWORD_EXPIRED: int
MAPI_E_PROFILE_DELETED: int
MAPI_E_RECONNECTED: int
MAPI_E_SESSION_LIMIT: int
MAPI_E_STORE_FULL: int
MAPI_E_STRING_TOO_LONG: int
MAPI_E_SUBMITTED: int
MAPI_E_TABLE_EMPTY: int
MAPI_E_TABLE_TOO_BIG: int
MAPI_E_TIMEOUT: int
MAPI_E_TOO_BIG: int
MAPI_E_TOO_COMPLEX: int
MAPI_E_TYPE_NO_SUPPORT: int
MAPI_E_UNABLE_TO_ABORT: int
MAPI_E_UNABLE_TO_COMPLETE: int
MAPI_E_UNCONFIGURED: int
MAPI_E_UNEXPECTED_ID: int
MAPI_E_UNEXPECTED_TYPE: int
MAPI_E_UNKNOWN_CPID: int
MAPI_E_UNKNOWN_ENTRYID: int
MAPI_E_UNKNOWN_FLAGS: int
MAPI_E_UNKNOWN_LCID: int
MAPI_E_USER_CANCEL: int
MAPI_E_VERSION: int
MAPI_E_WAIT: int
MAPI_EXPLICIT_PROFILE: int
MAPI_EXTENDED: int
MAPI_FOLDER: int
MAPI_FORCE_ACCESS: int
MAPI_FORCE_DOWNLOAD: int
MAPI_FORMINFO: int
MAPI_INIT_VERSION: int
MAPI_LOGON_UI: int
MAPI_MAILUSER: int
MAPI_MESSAGE: int
MAPI_MODIFY: int
MAPI_MOVE: int
MAPI_MULTITHREAD_NOTIFICATIONS: int
MAPI_NATIVE_BODY: int
MAPI_NATIVE_BODY_TYPE_HTML: int
MAPI_NATIVE_BODY_TYPE_PLAINTEXT: int
MAPI_NATIVE_BODY_TYPE_RTF: int
MAPI_NEW_SESSION: int
MAPI_NO_IDS: int
MAPI_NO_MAIL: int
MAPI_NO_STRINGS: int
MAPI_NOREPLACE: int
MAPI_NT_SERVICE: int
MAPI_P1: int
MAPI_PASSWORD_UI: int
MAPI_PROFSECT: int
MAPI_SERVICE_UI_ALWAYS: int
MAPI_SESSION: int
MAPI_STATUS: int
MAPI_STORE: int
MAPI_SUBMITTED: int
MAPI_TIMEOUT_SHORT: int
MAPI_TO: int
MAPI_UNICODE: int
MAPI_USE_DEFAULT: int
MAPI_W_APPROX_COUNT: int
MAPI_W_CANCEL_MESSAGE: int
MAPI_W_ERRORS_RETURNED: int
MAPI_W_NO_SERVICE: int
MAPI_W_PARTIAL_COMPLETION: int
MAPI_W_POSITION_CHANGED: int
MDB_NO_DIALOG: int
MDB_NO_MAIL: int
MDB_TEMPORARY: int
MDB_WRITE: int
MESSAGE_DIALOG: int
MODRECIP_ADD: int
MODRECIP_MODIFY: int
MODRECIP_REMOVE: int
NO_ATTACHMENT: int
OPEN_IF_EXISTS: int
PSTF_BEST_ENCRYPTION: int
PSTF_COMPRESSABLE_ENCRYPTION: int
PSTF_NO_ENCRYPTION: int
RELOP_EQ: int
RELOP_GE: int
RELOP_GT: int
RELOP_LE: int
RELOP_LT: int
RELOP_NE: int
RELOP_RE: int
RES_AND: int
RES_BITMASK: int
RES_COMMENT: int
RES_COMPAREPROPS: int
RES_CONTENT: int
RES_EXIST: int
RES_NOT: int
RES_OR: int
RES_PROPERTY: int
RES_SIZE: int
RES_SUBRESTRICTION: int
RTF_SYNC_BODY_CHANGED: int
RTF_SYNC_RTF_CHANGED: int
SERVICE_UI_ALLOWED: int
SERVICE_UI_ALWAYS: int
SHOW_SOFT_DELETES: int
SOF_UNIQUEFILENAME: int
STATUS_DEFAULT_STORE: int
STATUS_FLUSH_QUEUES: int
STATUS_INBOUND_FLUSH: int
STATUS_OUTBOUND_FLUSH: int
SUPPRESS_RECEIPT: int
TABLE_CHANGED: int
TABLE_ERROR: int
TABLE_RELOAD: int
TABLE_RESTRICT_DONE: int
TABLE_ROW_ADDED: int
TABLE_ROW_DELETED: int
TABLE_ROW_MODIFIED: int
TABLE_SETCOL_DONE: int
TABLE_SORT_ASCEND: int
TABLE_SORT_COMBINE: int
TABLE_SORT_DESCEND: int
TABLE_SORT_DONE: int
TBL_ALL_COLUMNS: int
TBL_ASYNC: int
TBL_BATCH: int
CLSID_IConverterSession: _win32typing.PyIID
CLSID_MailMessage: _win32typing.PyIID
IID_IABContainer: _win32typing.PyIID
IID_IAddrBook: _win32typing.PyIID
IID_IAttachment: _win32typing.PyIID
IID_IConverterSession: _win32typing.PyIID
IID_IDistList: _win32typing.PyIID
IID_IMAPIAdviseSink: _win32typing.PyIID
IID_IMAPIContainer: _win32typing.PyIID
IID_IMAPIFolder: _win32typing.PyIID
IID_IMAPIProp: _win32typing.PyIID
IID_IMAPISession: _win32typing.PyIID
IID_IMAPIStatus: _win32typing.PyIID
IID_IMAPITable: _win32typing.PyIID
IID_IMailUser: _win32typing.PyIID
IID_IMessage: _win32typing.PyIID
IID_IMsgServiceAdmin: _win32typing.PyIID
IID_IMsgServiceAdmin2: _win32typing.PyIID
IID_IMsgStore: _win32typing.PyIID
IID_IProfAdmin: _win32typing.PyIID
IID_IProfSect: _win32typing.PyIID
IID_IProviderAdmin: _win32typing.PyIID
MAPI_DISTLIST: int
MSPST_UID_PROVIDER: _win32typing.PyIID
PSETID_Address: _win32typing.PyIID
PSETID_AirSync: _win32typing.PyIID
PSETID_Appointment: _win32typing.PyIID
PSETID_Common: _win32typing.PyIID
PSETID_Log: _win32typing.PyIID
PSETID_Meeting: _win32typing.PyIID
PSETID_Messaging: _win32typing.PyIID
PSETID_Note: _win32typing.PyIID
PSETID_PostRss: _win32typing.PyIID
PSETID_Remote: _win32typing.PyIID
PSETID_Report: _win32typing.PyIID
PSETID_Sharing: _win32typing.PyIID
PSETID_Task: _win32typing.PyIID
PSETID_UnifiedMessaging: _win32typing.PyIID
PS_INTERNET_HEADERS: _win32typing.PyIID
PS_MAPI: _win32typing.PyIID
PS_PUBLIC_STRINGS: _win32typing.PyIID
PS_ROUTING_ADDRTYPE: _win32typing.PyIID
PS_ROUTING_DISPLAY_NAME: _win32typing.PyIID
PS_ROUTING_EMAIL_ADDRESSES: _win32typing.PyIID
PS_ROUTING_ENTRYID: _win32typing.PyIID
PS_ROUTING_SEARCH_KEY: _win32typing.PyIID
