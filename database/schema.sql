CREATE TYPE leave_type AS ENUM (
    'Paid',
    'Sick',
    'Unpaid'
);

CREATE TYPE leave_status AS ENUM (
    'Pending',
    'Approved',
    'Rejected'
);

CREATE TYPE user_role AS ENUM (
    'Employee',
    'Admin',
    'HR'
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role user_role NOT NULL DEFAULT 'Employee',
    department VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE leave_balances (
    id BIGSERIAL PRIMARY KEY,

    employee_id BIGINT NOT NULL,

    CONSTRAINT fk_leave_balance_employee
        FOREIGN KEY (employee_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    paid_leave INTEGER NOT NULL DEFAULT 0,
    sick_leave INTEGER NOT NULL DEFAULT 0,

    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(employee_id)
);

CREATE TABLE leave_requests (
    id BIGSERIAL PRIMARY KEY,

    employee_id BIGINT NOT NULL,

    CONSTRAINT fk_leave_request_employee
        FOREIGN KEY (employee_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    leave_type leave_type NOT NULL,

    start_date DATE NOT NULL,
    end_date DATE NOT NULL,

    remarks TEXT,

    status leave_status NOT NULL DEFAULT 'Pending',

    admin_comment TEXT,

    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT valid_date_range
        CHECK (end_date >= start_date)
);