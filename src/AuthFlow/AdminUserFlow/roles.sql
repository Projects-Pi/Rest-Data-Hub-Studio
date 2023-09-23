-- Insert Admin role with full CRUD permissions
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Admin', TRUE, TRUE, TRUE, TRUE);

-- Insert Editor role with create, read, and update permissions
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Editor', TRUE, TRUE, TRUE, FALSE);

-- Insert Viewer role with read-only permissions
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Viewer', FALSE, TRUE, FALSE, FALSE);

-- Insert Owner role with full CRUD permissions
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Owner', TRUE, TRUE, TRUE, TRUE);

-- Insert Moderator role with create, read, and update permissions
-- This role might also have delete permissions for specific cases
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Moderator', TRUE, TRUE, TRUE, FALSE);

-- Insert Guest role with read-only permissions
INSERT INTO roles (name, can_create, can_read, can_update, can_delete)
VALUES ('Guest', FALSE, TRUE, FALSE, FALSE);
